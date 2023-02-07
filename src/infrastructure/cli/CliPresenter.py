from src.domain.NaturalLanguageToolkit import NaturalLanguageToolkit
from src.infrastructure.FileHandler import FileHandler
from src.infrastructure.cli.ApplicationMessages import *


class CliPresenter:

    file_handler = FileHandler()

    def show_introduction(self):
        print(welcome_message)

    def show_options(self):
        print(tokenize_text_option)
        print(tokenize_sentence_option)
        print(remove_stopwords_option)
        print(count_total_words_option)
        print(count_repetitions_option)
        print(most_repeated_word_option)
        print(close_program_option)
        print(display_info_option)
        user_option = input(select_option_message)
        return user_option

    def tokenize_text(self):
        print(tokenize_text_select_file)
        content_to_process = self.extract_content_from_file()
        if len(content_to_process) != 0:
            natural_language_toolkit = NaturalLanguageToolkit()
            processed_content = natural_language_toolkit.tokenize_text(content_to_process)
            output_file_path = "/home/eaviles/Desktop/processed.txt"
            self.file_handler.write(output_file_path, processed_content)
            print(tokenize_file_succeeded, output_file_path)
        else:
            print(file_empty_or_not_found)

    def tokenize_sentence(self):
        print(tokenize_sentence_select_file)
        content_to_process = self.extract_content_from_file()
        if len(content_to_process) != 0:
            natural_language_toolkit = NaturalLanguageToolkit()
            processed_content = natural_language_toolkit.tokenize_sentence(content_to_process)
            output_file_path = "/home/eaviles/Desktop/processed.txt"
            self.file_handler.write(output_file_path, processed_content)
            print(tokenize_file_succeeded, output_file_path)
        else:
            print(file_empty_or_not_found)

    def remove_stopwords(self):
        print(remove_stopwords_select_file)
        content_to_process = self.extract_content_from_file()
        if len(content_to_process) != 0:
            natural_language_toolkit = NaturalLanguageToolkit()
            processed_content = natural_language_toolkit.remove_stopwords(content_to_process, "spanish")
            output_file_path = "/home/eaviles/Desktop/processed.txt"
            self.file_handler.write(output_file_path, processed_content)
            print(remove_stopwords_succeeded, output_file_path)
        else:
            print(file_empty_or_not_found)

    def count_total_words(self):
        print(count_total_words_select_file)
        content_to_process = self.extract_content_from_file()
        if len(content_to_process) != 0:
            natural_language_toolkit = NaturalLanguageToolkit()
            total_words = natural_language_toolkit.count_total_words(content_to_process)
            print(count_total_words_succeeded % str(total_words))
        else:
            print(file_empty_or_not_found)

    def count_repetitions_of_a_word(self):
        print(count_repetitions_select_file)
        content_to_process = self.extract_content_from_file()
        if len(content_to_process) != 0:
            natural_language_toolkit = NaturalLanguageToolkit()
            word_to_search_for = input(count_repetitions_input_message)
            number_of_repetitions = natural_language_toolkit.count_repetitions_of_a_word(content_to_process, word_to_search_for)
            print(count_repetitions_succeeded % (word_to_search_for, str(number_of_repetitions)))
        else:
            print(file_empty_or_not_found)

    def find_most_repeated_word(self):
        print(most_repeated_word_select_file)
        content_to_process = self.extract_content_from_file()
        if len(content_to_process) != 0:
            natural_language_toolkit = NaturalLanguageToolkit()
            most_repeated_word = natural_language_toolkit.find_most_repeated_word(content_to_process)
            print(most_repeated_word_succeeded, most_repeated_word)
        else:
            print(file_empty_or_not_found)

    def display_option_not_valid_dialogue(self):
        print(invalid_option_message)

    def extract_content_from_file(self):
        file_path = input(path_to_file_message)
        content_to_process = self.file_handler.read(file_path)
        return content_to_process

    def ask_user_what_to_do_next(self):
        print(next_option_message)

    def display_close_program_message(self):
        print(farewell_message)
        print(credits_message)

    def display_information(self):
        print(divider_start)
        print(display_info_title)
        print(tokenize_text_info)
        print(tokenize_sentence_info)
        print(remove_stopwords_info)
        print(count_total_words_info)
        print(count_repetitions_info)
        print(most_repeated_word_info)
        print(divider_end)
