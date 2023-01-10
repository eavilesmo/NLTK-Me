from src.infrastructure.cli.CliPresenter import CliPresenter


class NltkMeCliExecutor:

    cli_presenter = CliPresenter()

    def show_introduction(self):
        self.cli_presenter.show_introduction()

    def choose_action(self):
        user_option = self.cli_presenter.show_options()
        self.interpret_user_input(user_option)

    def interpret_user_input(self, user_option):
        # Replace valid_user_options with a range instead
        valid_user_options = ["1", "2", "3", "4", "5", "6", "7"]
        while user_option not in valid_user_options:
            self.cli_presenter.display_option_not_valid_dialogue()
            self.cli_presenter.show_options()

        if user_option == "1":
            self.cli_presenter.tokenize_text()
            self.cli_presenter.ask_user_what_to_do_next()
            self.choose_action()
        elif user_option == "2":
            self.cli_presenter.tokenize_sentence()
            self.cli_presenter.ask_user_what_to_do_next()
            self.choose_action()
        elif user_option == "3":
            self.cli_presenter.remove_stopwords()
            self.cli_presenter.ask_user_what_to_do_next()
            self.choose_action()
        elif user_option == "4":
            self.cli_presenter.count_total_words()
            self.cli_presenter.ask_user_what_to_do_next()
            self.choose_action()
        elif user_option == "5":
            self.cli_presenter.count_repetitions_of_a_word()
            self.cli_presenter.ask_user_what_to_do_next()
            self.choose_action()
        elif user_option == "6":
            self.cli_presenter.find_most_repeated_word()
            user_input = self.cli_presenter.ask_user_what_to_do_next()
            self.interpret_user_input(user_input)
        elif user_option == "7":
            self.cli_presenter.display_close_program_message()
