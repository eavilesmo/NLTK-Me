class NltkMeCliExecutor():

    def show_introduction(self):
        cli_presenter = CliPresenter()
        cli_presenter.show_introduction()

    def choose_action(self):
        cli_presenter = CliPresenter()
        user_option = cli_presenter.choose_action()
        if user_option == 1:
            cli_presenter.tokenize_text()
        elif user_option == 2:
            cli_presenter.tokenize_sentence()

