from setuptools import setup, find_packages

setup(
    name='promptengineers',
    version='0.1.1',
    packages=find_packages(),
    install_requires=[
        # Common dependencies for all sub-packages
    ],
    extras_require={
        'history': ['fastapi', 'uvicorn'],  # Dependencies specific to the history sub-package
        # Add other sub-package specific dependencies here
    },
    author='Ryan Eggleston',
    author_email='kre8mymedia@gmail.com',
    description='A collection of utilities by Prompt Engineers',
    long_description=open('README.md', encoding='utf-8').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/promptengineers-ai/modules',
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
