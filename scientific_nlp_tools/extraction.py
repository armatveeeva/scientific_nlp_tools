"""
Entity extraction and keyword generation module.
"""

import yake
from typing import List, Dict, Optional

try:
    from chemdataextractor import Document

    HAS_CDE = True
except ImportError:
    HAS_CDE = False


class ChemicalEntityExtractor:
    """
    Chemical entity extractor using ChemDataExtractor (optional).

    Note: Requires 'chemdataextractor' to be installed.
    Install with: pip install scientific-nlp-tools[chem]
    """

    def __init__(self):
        if not HAS_CDE:
            raise ImportError(
                "ChemDataExtractor is not installed. "
                "Please install it manually or use: pip install scientific-nlp-tools[chem]"
            )

    def extract(self, text: str) -> Dict:
        """
        Extract chemical entities from text.

        Args:
            text: Input text containing chemical entities

        Returns:
            Dictionary with extracted entities (compounds, roles, etc.)
        """
        doc = Document(text)
        entities = {
            "compounds": [str(c) for c in doc.cems],
            "roles": [str(r) for r in doc.roles],
        }
        return entities


class KeywordGenerator:
    """
    Keyword generator using YAKE algorithm.

    Example:
        generator = KeywordGenerator(language="ru", max_ngram_size=3)
        keywords = generator.generate(text, num_keywords=10)
    """

    def __init__(
            self,
            language: str = "ru",
            max_ngram_size: int = 3,
            deduplication_threshold: float = 0.1
    ):
        """
        Initialize the keyword generator.

        Args:
            language: Language code (ru, en, etc.)
            max_ngram_size: Maximum n-gram size for keywords
            deduplication_threshold: Threshold for deduplication
        """
        self.kw_extractor = yake.KeywordExtractor(
            lan=language,
            n=max_ngram_size,
            dedupLim=deduplication_threshold,
            top=20
        )

    def generate(self, text: str, num_keywords: int = 10) -> List[str]:
        """
        Generate keywords from text.

        Args:
            text: Input text
            num_keywords: Number of keywords to return

        Returns:
            List of keyword strings
        """
        keywords = self.kw_extractor.extract_keywords(text)
        return [kw for kw, score in keywords[:num_keywords]]
