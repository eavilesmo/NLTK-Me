from src.domain import TextProcessingTools
from src.infrastructure import FileHandler


class Presenter:

    def __init__(self, text_processing_tools: TextProcessingTools, file_handler: FileHandler):
        self.text_processing_tools = text_processing_tools
        self.file_handler = file_handler

