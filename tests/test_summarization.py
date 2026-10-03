"""
Tests for the TextSummarizer module.
"""
import pytest
from scientific_nlp_tools.summarization import TextSummarizer


def test_summarizer_initialization():
    """Проверка корректной инициализации суммаризатора."""
    summarizer = TextSummarizer(language="russian")
    assert summarizer.language == "russian"


def test_summarizer_short_text():
    """Проверка работы с очень коротким текстом (fallback)."""
    summarizer = TextSummarizer(language="russian")
    text = "Это очень короткий текст."
    result = summarizer.summarize(text, sentences_count=2)

    assert len(result) > 0
    assert "короткий текст" in result.lower()


def test_summarizer_long_text():
    """Проверка извлечения нужного количества предложений."""
    summarizer = TextSummarizer(language="russian")
    text = (
        "Первое важное предложение о машинном обучении. "
        "Второе предложение рассказывает о нейронных сетях. "
        "Третье предложение упоминает FAISS и векторный поиск. "
        "Четвертое предложение говорит о производительности."
    )
    result = summarizer.summarize(text, sentences_count=2)

    assert len(result) < len(text)
    assert len(result) > 20
