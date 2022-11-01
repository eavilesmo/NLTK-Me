import unittest
from doubles import allow

from src.TextProcessingTools import TextProcessingTools


class TestNltkApp(unittest.TestCase):

    def test_tokenize_text(self):
        get_file_path = ""
        filename_path = ""
        text_processing_tools = TextProcessingTools()

        allow(text_processing_tools).tokenize_text(get_file_path, filename_path).and_return("Hello")

        self.assertEqual(text_processing_tools.tokenize_text(get_file_path, filename_path), "Hello")


if __name__ == '__main__':
    unittest.main()
