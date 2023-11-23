from setuptools import setup, find_packages

setup(
    name='promptengineers',
    version='0.1.2',
    packages=find_packages(),
    install_requires=[
        'ujson'
    ],
    extras_require={
        'history': ['fastapi', 'uvicorn', 'motor', 'pymongo', 'cryptography'],
        'storage': ['fastapi', 'uvicorn', 'minio', 'python-multipart'],
    },
    author='Ryan Eggleston',
    author_email='kre8mymedia@gmail.com',
    description='A collection of utilities by Prompt Engineers',
    long_description=open('README.md', encoding='utf-8').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/promptengineers-ai/core',
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
