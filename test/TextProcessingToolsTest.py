import unittest
from doublex import Stub, assert_that, when, ANY_ARG
from hamcrest import equal_to

from src.infrastructure.FileHandler import FileHandler
from src.domain.TextProcessingTools import TextProcessingTools


class TextProcessingToolsTest(unittest.TestCase):

    def test_tokenize_text(self):
        content_to_tokenize = "This is a sentence. This is a second sentence."
        text_processing_tools = TextProcessingTools()

        actual_result = text_processing_tools.tokenize_text(content_to_tokenize)

        expected_result = ["This is a sentence.", "This is a second sentence."]
        assert_that(actual_result, equal_to(expected_result))

    def test_tokenize_sentence(self):
        text_processing_tools = TextProcessingTools()
        content_to_tokenize = "This is a sentence."

        actual_tokenized_sentence = text_processing_tools.tokenize_sentence(content_to_tokenize)

        expected_tokenized_sentence = ["This", "is", "a", "sentence", "."]
        assert_that(actual_tokenized_sentence, equal_to(expected_tokenized_sentence))

    def test_remove_stopwords(self):
        text_processing_tools = TextProcessingTools()
        content_to_process = "The stopwords from this sentence will be removed"
        stopwords_language = "english"

        actual_processed_text = text_processing_tools.remove_stopwords(content_to_process, stopwords_language)

        expected_processed_text = ["stopwords", "sentence", "removed"]
        assert_that(actual_processed_text, equal_to(expected_processed_text))

    def test_count_total_words(self):
        text_processing_tools = TextProcessingTools()
        content_to_process = "Testing now this method"

        actual_wordcount = text_processing_tools.count_total_words(content_to_process)

        expected_wordcount = 4
        assert_that(actual_wordcount, equal_to(expected_wordcount))

    def test_count_repetitions_of_a_word(self):
        text_processing_tools = TextProcessingTools()
        content_to_process = "This is a test, not a potato, not a carrot"
        word_to_search_for = "a"

        actual_count = text_processing_tools.count_repetitions_of_a_word(content_to_process, word_to_search_for)

        expected_count = 3
        assert_that(actual_count, equal_to(expected_count))

    def test_find_most_repeated_word(self):
        text_processing_tools = TextProcessingTools()
        content_to_process = "This is a test, not a potato, not a carrot"

        actual_most_repeated_word = text_processing_tools.find_most_repeated_word(content_to_process)

        expected_most_repeated_word = "a"
        assert_that(actual_most_repeated_word, equal_to(expected_most_repeated_word))


if __name__ == '__main__':
    unittest.main()
