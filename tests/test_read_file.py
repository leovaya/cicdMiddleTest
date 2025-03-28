import pytest
from text_analyzer import TextAnalyzer

@pytest.fixture
def create_temp_file(tmp_path):
    def _create(content):
        file = tmp_path / "test_file.txt"
        file.write_text(content, encoding="utf-8")
        return file
    return _create

@pytest.mark.parametrize("content", ["Test file content.", "  Another test.  ", ""])
def test_read_file(create_temp_file, content):
    file_path = create_temp_file(content)
    analyzer = TextAnalyzer(str(file_path))
    assert analyzer._TextAnalyzer__read_file(str(file_path)) == content.strip()
