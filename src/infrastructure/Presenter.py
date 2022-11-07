from src.domain import TextProcessingTools
from src.infrastructure import FileHandler


class Presenter:

    def __init__(self, text_processing_tools: TextProcessingTools, file_handler: FileHandler):
        self.text_processing_tools = text_processing_tools
        self.file_handler = file_handler

    def tokenize_text(self, file, filename_path):
        content_to_tokenize = self.file_handler.read_file(file)
        tokenized_content = self.text_processing_tools.tokenize_text(content_to_tokenize)
        if len(tokenized_content) <= 0:
            return "The file is empty."
        self.file_handler.write(filename_path, tokenized_content)

    def tokenize_sentence(self, file, filename_path):
        content_to_tokenize = self.file_handler.read_file(file)
        tokenized_content = self.text_processing_tools.tokenize_sentence(content_to_tokenize)
        if len(tokenized_content) <= 0:
            return "The file is empty."
        self.file_handler.write(filename_path, tokenized_content)
