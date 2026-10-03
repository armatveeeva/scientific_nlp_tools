"""
Text summarization module using TextRank algorithm.
"""

from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.text_rank import TextRankSummarizer
from typing import Optional


class TextSummarizer:
    """
    Extractive text summarizer using TextRank algorithm.

    Example:
        summarizer = TextSummarizer(language="russian")
        summary = summarizer.summarize(long_text, sentences_count=2)
    """

    def __init__(self, language: str = "russian"):
        """
        Initialize the summarizer.

        Args:
            language: Language for tokenization (default: russian)
        """
        self.summarizer = TextRankSummarizer()
        self.language = language

    def summarize(self, text: str, sentences_count: int = 2) -> str:
        """
        Summarize the input text.

        Args:
            text: Input text to summarize
            sentences_count: Number of sentences in summary

        Returns:
            Summarized text
        """
        try:
            parser = PlaintextParser.from_string(text, Tokenizer(self.language))
            summary = self.summarizer(parser.document, sentences_count=sentences_count)
            return " ".join([str(sentence) for sentence in summary])
        except Exception:
            return text.split('. ')[0] + '.'
