from src.infrastructure.cli.CliPresenter import CliPresenter


class NltkMeCliExecutor:

    def show_introduction(self):
        cli_presenter = CliPresenter()
        cli_presenter.show_introduction()

    def choose_action(self):
        cli_presenter = CliPresenter()
        user_option = cli_presenter.show_options()
        if user_option == 1:
            cli_presenter.tokenize_text()

