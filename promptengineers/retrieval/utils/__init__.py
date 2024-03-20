import requests
import ujson
from typing import Union, Literal
from urllib.parse import urljoin, urlparse

from bs4 import BeautifulSoup
from langchain.callbacks import get_openai_callback
from langchain_openai import OpenAIEmbeddings
from langchain.vectorstores import FAISS
from langchain.text_splitter import (
	CharacterTextSplitter, RecursiveCharacterTextSplitter, SpacyTextSplitter,
	PythonCodeTextSplitter, MarkdownTextSplitter, NLTKTextSplitter,
	LatexTextSplitter, TokenTextSplitter, SentenceTransformersTokenTextSplitter
)
from promptengineers.core.config import REDIS_URL
import aioredis

class CacheService:
	_instance = None

	def __new__(cls, *args, **kwargs):
		if not cls._instance:
			cls._instance = super(CacheService, cls).__new__(cls)
		return cls._instance

	def __init__(self, _url):
		self.url = _url
		self.redis = aioredis.from_url(self.url)
		
	async def publish(self, channel: str, message: str):
		return await self.redis.publish(channel, message)
	
cache = CacheService(REDIS_URL) if REDIS_URL else None

from promptengineers.core.utils import logger

def get_links(url: str):
	response = requests.get(url, timeout=5)
	soup = BeautifulSoup(response.text, 'html.parser')
	links = []
	for link in soup.find_all('a'):
		href = link.get('href')
		if href and urlparse(href).netloc == '':
			links.append(urljoin(url, href))
	return links

async def split_docs(
	pages,
	chunk_size: int = 1000,
	chunk_overlap: int = 100,
	splitter: Union[Literal['', 'recursive', 'spacy', 'nltk', 'python', 'latex', 'markdown', 'token', 'sentence']] = 'spacy',
	task_id: str = None,
):
	## Text Spliter
	if splitter == 'recursive':
		text_splitter = RecursiveCharacterTextSplitter(
			chunk_size=chunk_size,
			chunk_overlap=chunk_overlap
		)
	elif splitter == 'spacy':
		text_splitter = SpacyTextSplitter(
			chunk_size=chunk_size,
			chunk_overlap=chunk_overlap
		)
	elif splitter == 'nltk':
		text_splitter = NLTKTextSplitter(
			chunk_size=chunk_size,
			chunk_overlap=chunk_overlap
		)
	elif splitter == 'python':
		text_splitter = PythonCodeTextSplitter(
			chunk_size=chunk_size,
			chunk_overlap=chunk_overlap
		)
	elif splitter == 'markdown':
		text_splitter = MarkdownTextSplitter(
			chunk_size=chunk_size,
			chunk_overlap=chunk_overlap
		)
	elif splitter == 'latex':
		text_splitter = LatexTextSplitter(
			chunk_size=chunk_size,
			chunk_overlap=chunk_overlap
		)
	elif splitter == 'token':
		text_splitter = TokenTextSplitter(
			chunk_size=chunk_size,
			chunk_overlap=chunk_overlap
		)
	elif splitter == 'sentence': ## Install sentence-transformers (1gb+)
		text_splitter = SentenceTransformersTokenTextSplitter(
			chunk_size=chunk_size,
			chunk_overlap=chunk_overlap
		)
	elif splitter == 'character':
		text_splitter = CharacterTextSplitter(
			chunk_size=chunk_size,
			chunk_overlap=chunk_overlap
		)
	else:
		raise ValueError(f"Invalid splitter type: {splitter}")
	
	chunks = []
	for i, page in enumerate(pages):
		docs = text_splitter.split_documents([page])
		for index, doc in enumerate(docs):
			doc.metadata['section'] = index + 1
			doc.metadata['word_count'] = len(doc.page_content.split())
			doc.metadata['character_count'] = len(doc.page_content)
			# doc.metadata['splitter'] = {
			# 	'type': splitter,
			# 	'chunk_size': chunk_size,
			# 	'chunk_overlap': chunk_overlap
			# }
			chunks.append(doc)
		# Calculate progress percentage
		progress_percentage = (i + 1) / len(pages) * 100
		logger.debug(f'[utils.retrieval.split_docs] Progress: {progress_percentage:.2f}%')
		if cache:
			await cache.publish(
				task_id, 
				ujson.dumps({
					'step': 'end' if i+1 == len(pages) else 'split',
					'message': f'Created {len(chunks)} chunks from {len(pages)} pages.' if i+1 == len(pages) else f'Spliting page {i+1} into chunks',
					'progress': round(progress_percentage, 2), 
					'page_number': i + 1,
					'page_count': len(pages),
					'chunk_count': len(chunks)
				})
			)
	return chunks

def create_faiss_vectorstore(
	docs,
	chunk_size: int = 1000,
	chunk_overlap: int = 0
):
	"""Load the vectorstore."""
	with get_openai_callback() as callback:
		logger.info('[utils.retrieval.create_vectorstore] Tokens: %s', callback.total_tokens)
		embeddings = OpenAIEmbeddings(max_retries=2)
		return FAISS.from_documents(
			split_docs(docs, chunk_size, chunk_overlap),
			embeddings
		)
