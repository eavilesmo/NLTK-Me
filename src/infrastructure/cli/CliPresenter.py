from src.domain.NaturalLanguageToolkit import NaturalLanguageToolkit
from src.infrastructure.FileHandler import FileHandler


class CliPresenter:

    file_handler = FileHandler()

    def show_introduction(self):
        print("Welcome to NLTK-Me!\nWhat would you like to do?")

    def show_options(self):
        print("1. Tokenize a text")
        print("2. Tokenize a sentence")
        print("3. Remove stopwords")
        print("4. Count the total words of a text")
        print("5. Count how many times a word appears in a text")
        print("6. Find the most repeated word in a text")
        print("7. Close the program")
        print("Do you want to know more about the different options? Just type 'info'!")
        user_option = input("Introduce a number to select an option: ")
        return user_option

    def tokenize_text(self):
        print("Let's tokenize a text! Please introduce the path to the file you want to tokenize.")
        content_to_process = self.extract_content_from_file()
        if len(content_to_process) != 0:
            natural_language_toolkit = NaturalLanguageToolkit()
            processed_content = natural_language_toolkit.tokenize_text(content_to_process)
            output_file_path = "/home/eaviles/Desktop/processed.txt"
            self.file_handler.write(output_file_path, processed_content)
            print("Great! Your text has been tokenized! We have saved the output file here:\n" + output_file_path)
        else:
            print("The file is empty or was not found!")

    def tokenize_sentence(self):
        print("Let's tokenize some sentences! Please introduce the path to the file you want to tokenize.")
        content_to_process = self.extract_content_from_file()
        if len(content_to_process) != 0:
            natural_language_toolkit = NaturalLanguageToolkit()
            processed_content = natural_language_toolkit.tokenize_sentence(content_to_process)
            output_file_path = "/home/eaviles/Desktop/processed.txt"
            self.file_handler.write(output_file_path, processed_content)
            print("Great! Your text has been tokenized! We have saved the output file here:\n" + output_file_path)
        else:
            print("The file is empty or was not found!")

    def remove_stopwords(self):
        print("Let's remove stopwords! Please introduce the path to the file you want to process.")
        content_to_process = self.extract_content_from_file()
        if len(content_to_process) != 0:
            natural_language_toolkit = NaturalLanguageToolkit()
            processed_content = natural_language_toolkit.remove_stopwords(content_to_process, "spanish")
            output_file_path = "/home/eaviles/Desktop/processed.txt"
            self.file_handler.write(output_file_path, processed_content)
            print("Great! Your text has been processed! We have saved the output file here:\n" + output_file_path)
        else:
            print("The file is empty or was not found!")

    def count_total_words(self):
        print("Let's count words! Please introduce the path to the file you want to process.")
        content_to_process = self.extract_content_from_file()
        if len(content_to_process) != 0:
            natural_language_toolkit = NaturalLanguageToolkit()
            total_words = natural_language_toolkit.count_total_words(content_to_process)
            print("Great! Your file has " + str(total_words) + " words.")
        else:
            print("The file is empty or was not found!")

    def count_repetitions_of_a_word(self):
        print("Let's count how many times a word is repeated! Please introduce the path to the file you want to process.")
        content_to_process = self.extract_content_from_file()
        if len(content_to_process) != 0:
            natural_language_toolkit = NaturalLanguageToolkit()
            word_to_search_for = input("Now, please introduce the word you want to search for: ")
            number_of_repetitions = natural_language_toolkit.count_repetitions_of_a_word(content_to_process, word_to_search_for)
            print("Done! The word " + word_to_search_for + " appears " + str(number_of_repetitions) + " times.")
        else:
            print("The file is empty or was not found!")

    def find_most_repeated_word(self):
        print("Let's find the most repeated word! Please introduce the path to the file you want to process.")
        content_to_process = self.extract_content_from_file()
        if len(content_to_process) != 0:
            natural_language_toolkit = NaturalLanguageToolkit()
            most_repeated_word = natural_language_toolkit.find_most_repeated_word(content_to_process)
            print("We found it! The most repeated word is: " + most_repeated_word)
        else:
            print("The file is empty or was not found!")

    def display_option_not_valid_dialogue(self):
        print("\nSorry, the option you introduced is not correct. Please try again.")

    def extract_content_from_file(self):
        file_path = input("Path to file: ")
        content_to_process = self.file_handler.read(file_path)
        return content_to_process

    def ask_user_what_to_do_next(self):
        print("What would you like to do next?")

    def display_close_program_message(self):
        print("\nThank you! Have a good day! :)")
        print("\nNLTK-Me! CLI Version\nCreated by Macarena Avilés")

    def display_information(self):
        print("\n----------------------------------")
        print("Did you ask for some info? Here you go!")
        print("1. Tokenize a text: With Text Tokenizer, you can tokenize (split) a text into sentences. The text is split based on full stops. This option will create a file named 'processed.txt' in your desktop that will contain the result.")
        print("2. Tokenize a sentence: With Sentence Tokenizer, you can tokenize (split) a sentence into words. The sentences are split based on spaces. This option will create a file named 'processed.txt' in your desktop that will contain the result.")
        print("3. Remove stopwords: This function removes the stopwords from a text. This means that all words with no meaning in the text (as articles, prepositions or punctuation marks) will be removed from the text. This option will create a file named 'processed.txt' in your desktop that will contain the result.")
        print("4. Count the total words of a text: This function shows how many words are in the text. The result will be printed in the console.")
        print("5. Count how many times a word appears in a text: This function shows how many times a word appears in the text. The result will be printed in the console. lease note this function isn't case sensitive, which means that it differentiate between capital or lower-case letters.")
        print("6. Find the most repeated word in a text: This function simply shows the most repeated word in the text! The result will be printed in the console. It's recommended to first execute the function 'Remove stopwords' in the file to avoid getting strange results (for instance, getting articles, pronouns or even punctuation marks as the most frequent word.)")
        print("----------------------------------\n")
