import pytest
from text_analyzer import TextAnalyzer

@pytest.fixture
def create_temp_file(tmp_path):
    def _create(content):
        file = tmp_path / "test_file.txt"
        file.write_text(content, encoding="utf-8")
        return file
    return _create

@pytest.mark.parametrize("content, expected_text", [
    ("Hello world!", "Hello world!"),
    ("  This is a test.  ", "This is a test."),
    ("", ""),
])
def test_text_analyzer_init(create_temp_file, content, expected_text):
    file_path = create_temp_file(content)
    analyzer = TextAnalyzer(str(file_path))
    assert analyzer.text == expected_text