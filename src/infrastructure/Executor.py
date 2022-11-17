from src.domain.TextProcessingTools import TextProcessingTools
from src.infrastructure.FileHandler import FileHandler


class Executor:
    file_handler = FileHandler()
    text_processing_tools = TextProcessingTools()

    def tokenize_text(self, filepath_to_read, filepath_to_save):
        content_to_tokenize = self.file_handler.read_file(filepath_to_read)
        tokenized_content = self.text_processing_tools.tokenize_text(content_to_tokenize)
        if len(tokenized_content) <= 0:
            return "The file is empty."
        self.file_handler.write(filepath_to_save, tokenized_content)

    def tokenize_sentence(self, filepath_to_read, filepath_to_save):
        content_to_tokenize = self.file_handler.read_file(filepath_to_read)
        tokenized_content = self.text_processing_tools.tokenize_sentence(content_to_tokenize)
        if len(tokenized_content) <= 0:
            return "The file is empty."
        self.file_handler.write(filepath_to_save, tokenized_content)

    def remove_stopwords(self, filepath_to_read, filepath_to_save, language_of_text):
        content_to_process = self.file_handler.read_file(filepath_to_read)
        processed_content = self.text_processing_tools.remove_stopwords(content_to_process, language_of_text)
        if len(processed_content) <= 0:
            return "The file is empty."
        self.file_handler.write(filepath_to_save, processed_content)

    def count_total_words(self, filepath_to_read):
        content_to_process = self.file_handler.read_file(filepath_to_read)
        total_words = self.text_processing_tools.count_total_words(content_to_process)
        if len(total_words) <= 0:
            return "The file is empty."

    def count_repetitions_of_a_word(self, filepath_to_read, word_to_search_for):
        content_to_process = self.file_handler.read_file(filepath_to_read)
        number_of_repetitions = self.text_processing_tools.count_repetitions_of_a_word(content_to_process, word_to_search_for)
        if len(number_of_repetitions) <= 0:
            return "The file is empty."

    def find_most_repeated_word(self, filepath_to_read):
        content_to_process = self.file_handler.read_file(filepath_to_read)
        most_repeated_word = self.text_processing_tools.find_most_repeated_word(content_to_process)
        if len(most_repeated_word) <= 0:
            return "The file is empty."
