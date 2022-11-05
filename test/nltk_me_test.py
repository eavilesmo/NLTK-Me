import unittest
from doublex import Stub, assert_that, Mock, when, ANY_ARG
from hamcrest import is_, equal_to

from src.FileHandler import FileHandler
from src.TextProcessingTools import TextProcessingTools


class TestNltkApp(unittest.TestCase):

    def test_tokenize_text(self):
        file_content = "This is a sentence. This is a second sentence."
        get_file_path = "any_path"
        filename_path = "any_file_name_path"
        expected_result = ["This is a sentence.", "This is a second sentence."]

        with Stub(FileHandler) as stub:
            when(stub).readFile(get_file_path).returns(file_content)
            stub.write(filename_path, expected_result)
            text_processing_tools = TextProcessingTools(stub)
            actual_result = text_processing_tools.tokenize_text(get_file_path, filename_path)

        assert_that(actual_result, equal_to(expected_result))

    # def test_tokenize_sentence(self):
    #     file_content = "This is a sentence."
    #     get_file_path = "any_path"
    #     filename_path = "any_file_name_path"
    #     expected_tokenized_sentence = "This\nis\na\nsentence."
    #     text_processing_tools = TextProcessingTools()
    #
    #     with Stub(FileHandler) as stub:
    #         stub.readFile(get_file_path).returns(file_content)
    #         stub.write(filename_path, expected_tokenized_sentence)
    #
    #     actual_tokenized_sentence = text_processing_tools.tokenize_sentence(get_file_path, filename_path)
    #
    #     assert_that(actual_tokenized_sentence, equal_to(expected_tokenized_sentence))


if __name__ == '__main__':
    unittest.main()
