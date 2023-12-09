"""Request Models"""
from typing import Any, List, Optional, Union
from pydantic import BaseModel, Field

from promptengineers.models.loader import (
    TypeUrlLoader,
    YoutubeLoader,
    BlockchainLoader,
    CopyPasteLoader,
)

class RequestMultiLoader(BaseModel):
    index_name: str = Field(...)
    provider: str = ("pinecone", "redis")
    files: List[str] or None = Field(...)
    loaders: List[
        Union[TypeUrlLoader, YoutubeLoader, BlockchainLoader, CopyPasteLoader]
    ] or None = Field(...)

    class Config:
        json_schema_extra = {
            "example": {
                "provider": "pinecone",
                "index_name": "formio-docs-and-website",
                "files": [
                    "formio-customer-issue.pdf",
                ],
                "loaders": [
                    {"type": "gitbook", "urls": ["https://help.form.io"]},
                    {"type": "web_base", "urls": ["https://form.io"]},
                ],
            }
        }


class RequestDataLoader(BaseModel):
    index_name: str = Field(...)
    provider: str = ("pinecone", "redis")
    loaders: List[
        Union[TypeUrlLoader, YoutubeLoader, BlockchainLoader, CopyPasteLoader]
    ] or None = Field(...)

    class Config:
        json_schema_extra = {
            "example": {
                "provider": "pinecone",
                "index_name": "formio-docs-and-website",
                "loaders": [
                    {"type": "gitbook", "urls": ["https://help.form.io"]},
                    {"type": "web_base", "urls": ["https://form.io"]},
                    {"type": "copy", "text": "This is a test."},
                ],
            }
        }