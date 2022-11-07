import unittest
from doublex import Stub, assert_that, when, ANY_ARG
from hamcrest import equal_to

from src.FileHandler import FileHandler
from src.domain.TextProcessingTools import TextProcessingTools


class TestNltkApp(unittest.TestCase):

    def test_tokenize_text(self):
        file_content = "This is a sentence. This is a second sentence."
        get_file_path = "any_path"
        filename_path = "any_file_name_path"
        expected_result = ["This is a sentence.", "This is a second sentence."]

        with Stub(FileHandler) as stub:
            when(stub).read_file(ANY_ARG).returns(file_content)
            stub.write(ANY_ARG)
            text_processing_tools = TextProcessingTools(stub)
            actual_result = text_processing_tools.tokenize_text(get_file_path, filename_path)

        assert_that(actual_result, equal_to(expected_result))

    def test_tokenize_sentence(self):
        file_content = "This is a sentence."
        get_file_path = "any_path"
        filename_path = "any_file_name_path"
        expected_tokenized_sentence = ["This", "is", "a", "sentence", "."]

        with Stub(FileHandler) as stub:
            when(stub).read_file(ANY_ARG).returns(file_content)
            stub.write(ANY_ARG)
            text_processing_tools = TextProcessingTools(stub)
            actual_tokenized_sentence = text_processing_tools.tokenize_sentence(get_file_path, filename_path)

        assert_that(actual_tokenized_sentence, equal_to(expected_tokenized_sentence))

    def test_stopwords_remover(self):
        file_content = "The stopwords from this sentence will be removed"
        get_file_path = "any_path"
        filename_path = "any_file_name_path"
        stopwords_language = "english"
        expected_processed_text = ["stopwords", "sentence", "removed"]

        with Stub(FileHandler) as stub:
            when(stub).read_file(ANY_ARG).returns(file_content)
            text_processing_tools = TextProcessingTools(stub)
            actual_processed_text = text_processing_tools.stopwords_remover(get_file_path,
                                                                            filename_path, stopwords_language)

        assert_that(actual_processed_text, equal_to(expected_processed_text))

    def test_total_words_count(self):
        file_content = "Testing now this method"
        expected_wordcount = 4
        get_file_path = "any_path"

        with Stub(FileHandler) as stub:
            when(stub).read_file(ANY_ARG).returns(file_content)
            text_processing_tools = TextProcessingTools(stub)
            actual_wordcount = text_processing_tools.total_words_count(get_file_path)

        assert_that(actual_wordcount, equal_to(expected_wordcount))

    def test_freqdist_count(self):
        file_content = "This is a test, not a potato, not a carrot"
        expected_count = 3
        get_file_path = "any_path"
        word_to_count = "a"

        with Stub(FileHandler) as stub:
            when(stub).read_file(ANY_ARG).returns(file_content)
            text_processing_tools = TextProcessingTools(stub)
            actual_count = text_processing_tools.freqdist_count(get_file_path, word_to_count)

        assert_that(actual_count, equal_to(expected_count))

    def test_freqdist_max(self):
        file_content = "This is a test, not a potato, not a carrot"
        get_file_path = "any_path"
        expected_most_repeated_word = "a"

        with Stub(FileHandler) as stub:
            when(stub).read_file(ANY_ARG).returns(file_content)
            text_processing_tools = TextProcessingTools(stub)
            actual_most_repeated_word = text_processing_tools.freqdist_max(get_file_path)

        assert_that(actual_most_repeated_word, equal_to(expected_most_repeated_word))


if __name__ == '__main__':
    unittest.main()
