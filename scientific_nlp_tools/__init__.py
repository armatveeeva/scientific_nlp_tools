"""
Scientific NLP Tools - Python library for scientific text processing.

Features:
- Semantic search using FAISS and Sentence Transformers
- Extractive text summarization using TextRank
- Chemical entity extraction using ChemDataExtractor
- Keyword generation using YAKE
"""

from .search import SemanticSearcher
from .summarization import TextSummarizer
from .extraction import ChemicalEntityExtractor, KeywordGenerator
from .preprocessing import TextCleaner

__version__ = "1.0.3"
__author__ = "Anastasiia Matveeva"
__email__ = "armatveeeva@gmail.com"
