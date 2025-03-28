import pytest
from text_analyzer import TextAnalyzer

@pytest.mark.parametrize("text, expected_count", [
    ("Hello world!", 1),
    ("First sentence. Second sentence!", 2),
    ("What? Really? Yes...", 3),
    ("No ending punctuation", 1),
    ("", 0),
])
def test_count_sentences(text, expected_count):
    analyzer = TextAnalyzer("")
    analyzer.text = text
    assert analyzer._TextAnalyzer__count_sentences() == expected_count
