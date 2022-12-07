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

    def tokenize_sentence(self):
        print("Let's tokenize some sentences! Please introduce the path to the file you want to tokenize.")
        file_path = input("Path to file: ")
        file_handler = FileHandler()
        content_to_process = file_handler.read(file_path)
        natural_language_toolkit = NaturalLanguageToolkit()
        processed_content = natural_language_toolkit.tokenize_sentence(content_to_process)
        output_file_path = "/home/eaviles/Desktop/processed.txt"
        file_handler.write(output_file_path, processed_content)
        print("Great! Your text has been tokenized! We have saved the output file here:\n" + output_file_path)

    def remove_stopwords(self):
        print("Let's remove stopwords! Please introduce the path to the file you want to process.")
        file_path = input("Path to file: ")
        file_handler = FileHandler()
        content_to_process = file_handler.read(file_path)
        natural_language_toolkit = NaturalLanguageToolkit()
        processed_content = natural_language_toolkit.remove_stopwords(content_to_process, "spanish")
        output_file_path = "/home/eaviles/Desktop/processed.txt"
        file_handler.write(output_file_path, processed_content)
        print("Great! Your text has been processed! We have saved the output file here:\n" + output_file_path)

    def count_total_words(self):
        print("Let's count words! Please introduce the path to the file you want to process.")
        file_path = input("Path to file: ")
        file_handler = FileHandler()
        content_to_process = file_handler.read(file_path)
        natural_language_toolkit = NaturalLanguageToolkit()
        total_words = natural_language_toolkit.count_total_words(content_to_process)
        print("Great! Your file has " + str(total_words) + " words.")

    def count_repetitions_of_a_word(self):
        print("Let's count how many times a word is repeated! Please introduce the path to the file you want to process.")
        file_path = input("Path to file: ")
        file_handler = FileHandler()
        content_to_process = file_handler.read(file_path)
        natural_language_toolkit = NaturalLanguageToolkit()
        word_to_search_for = input("Now, please introduce the word you want to search for: ")
        number_of_repetitions = natural_language_toolkit.count_repetitions_of_a_word(content_to_process, word_to_search_for)
        print("Done! The word " + word_to_search_for + " appears " + str(number_of_repetitions) + " times.")

    def find_most_repeated_word(self):
        print("Let's find the most repeated word! Please introduce the path to the file you want to process.")
        file_path = input("Path to file: ")
        file_handler = FileHandler()
        content_to_process = file_handler.read(file_path)
        natural_language_toolkit = NaturalLanguageToolkit()
        most_repeated_word = natural_language_toolkit.find_most_repeated_word(content_to_process)
        print("We found it! The most repeated word is: " + most_repeated_word)
