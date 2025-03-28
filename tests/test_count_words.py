import pytest
from text_analyzer import TextAnalyzer

@pytest.mark.parametrize("text, expected_count", [
    ("Hello world!", 2),
    ("This is a test, with some punctuation.", 7),
    ("One,two;three:four five", 5),
    ("", 0),
])
def test_count_words(text, expected_count):
    analyzer = TextAnalyzer("")
    analyzer.text = text
    assert analyzer._TextAnalyzer__count_words() == expected_count
