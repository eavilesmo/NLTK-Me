from src.domain.NaturalLanguageToolkit import NaturalLanguageToolkit
from src.infrastructure.gui.FileHandler import FileHandler


class CliPresenter:

    def show_introduction(self):
        print("Welcome to NLTK-Me!\nWhat would you like to do?")

    def show_options(self):
        print("1. Tokenize a text")
        user_option = input("Select an option: ")
        return user_option

    def tokenize_text(self):
        print("Let's tokenize a text! Please introduce the path to the file you want to tokenize.")
        file_path = input("Path to file: ")
        file_handler = FileHandler()
        content_to_process = file_handler.read(file_path)
        natural_language_toolkit = NaturalLanguageToolkit()
        processed_content = natural_language_toolkit.tokenize_text(content_to_process)
        output_file_path = "/home/eaviles/Desktop/processed.txt"
        file_handler.write(output_file_path, processed_content)
        print("Great! Your text has been tokenized! We have saved the output file here:\n" + output_file_path)
