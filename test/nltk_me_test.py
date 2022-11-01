import unittest
from doubles import allow

from src.TextProcessingTools import TextProcessingTools


class TestNltkApp(unittest.TestCase):

    def test_tokenize_text(self):
        get_file_path = ""
        filename_path = ""
        text_processing_tools = TextProcessingTools()
        expected_result = "Hello"
        allow(text_processing_tools).tokenize_text(get_file_path, filename_path).and_return("Hello")

        actual_result = text_processing_tools.tokenize_text(get_file_path, filename_path)

        self.assertEqual(actual_result, expected_result)


if __name__ == '__main__':
    unittest.main()
