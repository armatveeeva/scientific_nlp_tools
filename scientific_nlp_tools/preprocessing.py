"""
Text preprocessing utilities for scientific documents.
"""

import re
from typing import List


class TextCleaner:
    """
    Text cleaning and preprocessing utilities.

    Example:
        cleaner = TextCleaner()
        clean_text = cleaner.clean(raw_text)
    """

    def __init__(self):
        """Initialize the text cleaner."""
        pass

    def clean(self, text: str) -> str:
        """
        Clean text by removing extra whitespace and special characters.

        Args:
            text: Input text

        Returns:
            Cleaned text
        """
        text = re.sub(r'\s+', ' ', text)
        text = re.sub(r'[^\w\s.,;:!?()-]', '', text)
        return text.strip()

    def split_sentences(self, text: str) -> List[str]:
        """
        Split text into sentences.

        Args:
            text: Input text

        Returns:
            List of sentences
        """
        sentences = re.split(r'[.!?]+', text)
        return [s.strip() for s in sentences if s.strip()]
