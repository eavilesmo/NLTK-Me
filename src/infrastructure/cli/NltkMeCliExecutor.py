from src.infrastructure.cli.CliPresenter import CliPresenter


class NltkMeCliExecutor:

    def show_introduction(self):
        cli_presenter = CliPresenter()
        cli_presenter.show_introduction()

    def choose_action(self):
        cli_presenter = CliPresenter()
        user_option = cli_presenter.show_options()
        if user_option == "1":
            cli_presenter.tokenize_text()
        elif user_option == "2":
            cli_presenter.tokenize_sentence()
        elif user_option == "3":
            cli_presenter.remove_stopwords()
        elif user_option == "4":
            cli_presenter.count_total_words()

