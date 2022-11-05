import unittest
from doublex import Stub, assert_that
from hamcrest import equal_to, is_

from src.FileHandler import FileHandler
from src.TextProcessingTools import TextProcessingTools


class TestNltkApp(unittest.TestCase):

    def test_tokenize_text(self):
        file_content = "This is a sentence. This is a second sentence."
        get_file_path = "any_path"
        filename_path = "any_file_name_path"
        expected_result = "This is a sentence.\nThis is a second sentence."
        text_processing_tools = TextProcessingTools()

        with Stub(FileHandler) as stub:
            stub.readFile(get_file_path).returns(file_content)
            stub.write(filename_path, expected_result)

        actual_result = text_processing_tools.tokenize_text(get_file_path, filename_path)

        assert_that(actual_result), is_(expected_result)


if __name__ == '__main__':
    unittest.main()
