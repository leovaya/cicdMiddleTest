import pytest
from text_analyzer import TextAnalyzer

@pytest.mark.parametrize("text, expected_words, expected_sentences", [
    ("Hello world!", 2, 1),
    ("First sentence. Second sentence!", 4, 2),
    ("What? Really? Yes...", 3, 3),
    ("", 0, 0),
])
def test_analyze(text, expected_words, expected_sentences):
    analyzer = TextAnalyzer("")
    analyzer.text = text
    words, sentences = analyzer.analyze()
    assert words == expected_words
    assert sentences == expected_sentences
