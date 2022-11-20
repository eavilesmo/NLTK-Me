from src.domain import TextProcessingTools
from src.infrastructure import FileHandler


class Presenter:

    def __init__(self, text_processing_tools: TextProcessingTools, file_handler: FileHandler):
        self.text_processing_tools = text_processing_tools
        self.file_handler = file_handler

    def tokenize_text(self, file, filename_path):
        content_to_tokenize = self.file_handler.read(file)
        tokenized_content = self.text_processing_tools.tokenize_text(content_to_tokenize)
        if len(tokenized_content) <= 0:
            return "The file is empty."
        self.file_handler.write(filename_path, tokenized_content)

    def tokenize_sentence(self, file, filename_path):
        content_to_tokenize = self.file_handler.read(file)
        tokenized_content = self.text_processing_tools.tokenize_sentence(content_to_tokenize)
        if len(tokenized_content) <= 0:
            return "The file is empty."
        self.file_handler.write(filename_path, tokenized_content)

    def remove_stopwords(self, file, filename_path, language):
        content_to_process = self.file_handler.read(file)
        processed_content = self.text_processing_tools.remove_stopwords(content_to_process, language)
        if len(processed_content) <= 0:
            return "The file is empty."
        self.file_handler.write(filename_path, processed_content)

    def total_words_count(self, file):
        content_to_process = self.file_handler.read(file)
        total_words = self.text_processing_tools.count_total_words(content_to_process)
        if len(total_words) <= 0:
            return "The file is empty."

    def freqdist_count(self, file, word_to_search_for):
        content_to_process = self.file_handler.read(file)
        number_of_repetitions = self.text_processing_tools.count_repetitions_of_a_word(content_to_process, word_to_search_for)
        if len(number_of_repetitions) <= 0:
            return "The file is empty."

    def freqdist_max(self, file):
        content_to_process = self.file_handler.read(file)
        most_repeated_word = self.text_processing_tools.find_most_repeated_word(content_to_process)
        if len(most_repeated_word) <= 0:
            return "The file is empty."
