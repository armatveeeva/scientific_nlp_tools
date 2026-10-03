"""
Tests for the KeywordGenerator module.
"""
import pytest
from scientific_nlp_tools.extraction import KeywordGenerator


def test_keyword_generator_initialization():
    """Проверка инициализации генератора ключевых слов."""
    import yake
    generator = KeywordGenerator(language="ru", max_ngram_size=2)

    assert isinstance(generator.kw_extractor, yake.KeywordExtractor)

def test_keyword_generator_extraction():
    """Проверка извлечения ключевых слов из текста."""
    generator = KeywordGenerator(language="ru", max_ngram_size=3)
    text = "Машинное обучение и глубокие нейронные сети применяются для анализа больших данных в научных исследованиях."

    keywords = generator.generate(text, num_keywords=3)

    assert isinstance(keywords, list)
    assert len(keywords) <= 3
    assert any("машинное обучение" in kw.lower() or "нейронные сети" in kw.lower() for kw in keywords)
