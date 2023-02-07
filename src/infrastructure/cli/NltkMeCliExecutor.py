from src.infrastructure.cli.CliPresenter import CliPresenter
from src.infrastructure.cli.ApplicationMessages import *


class NltkMeCliExecutor:

    cli_presenter = CliPresenter()

    def show_introduction(self):
        self.cli_presenter.show_introduction()

    def choose_option(self):
        user_option = self.cli_presenter.show_options()
        self.interpret_user_option(user_option)

    def interpret_user_option(self, user_option):
        while user_option not in valid_user_options:
            self.cli_presenter.display_option_not_valid_dialogue()
            self.cli_presenter.show_options()

        if user_option == tokenize_text:
            self.cli_presenter.tokenize_text()
            self.choose_option()
        elif user_option == tokenize_sentence:
            self.cli_presenter.tokenize_sentence()
            self.choose_option()
        elif user_option == remove_stopwords:
            self.cli_presenter.remove_stopwords()
            self.choose_option()
        elif user_option == count_total_words:
            self.cli_presenter.count_total_words()
            self.cli_presenter.ask_user_what_to_do_next()
            self.choose_option()
        elif user_option == count_repetitions_of_a_word:
            self.cli_presenter.count_repetitions_of_a_word()
            self.choose_option()
        elif user_option == find_most_repeated_word:
            self.cli_presenter.find_most_repeated_word()
            self.choose_option()
        elif user_option == close_program:
            self.cli_presenter.display_close_program_message()
        elif user_option == information:
            self.cli_presenter.display_information()
            self.choose_option()
