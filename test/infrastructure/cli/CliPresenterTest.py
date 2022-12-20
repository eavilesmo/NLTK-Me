from src.infrastructure.cli.CliPresenter import CliPresenter

cli_presenter = CliPresenter()


def test_show_introduction(capsys):
    cli_presenter.show_introduction()
    captured = capsys.readouterr()
    expected_output = "Welcome to NLTK-Me!\nWhat would you like to do?"
    assert captured.out == expected_output


