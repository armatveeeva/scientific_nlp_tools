from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="scientific_nlp_tools",
    version="1.0.1",
    author="Anastasiia Armatveeva",
    author_email="armatveeva@rosatom.ru",
    description="Python library for scientific text processing: semantic search, summarization, entity extraction, and keyword generation",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/armatveeeva/scientific_nlp_tools",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
    ],
    python_requires=">=3.8",
    install_requires=[
        "faiss-cpu>=1.7.0",
        "sentence-transformers>=2.0.0",
        "sumy>=0.10.0",
        "yake>=0.4.0",
        "numpy<2.0.0",
    ],
)
