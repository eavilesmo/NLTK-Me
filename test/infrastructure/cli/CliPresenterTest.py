from src.infrastructure.cli.CliPresenter import CliPresenter

cli_presenter = CliPresenter()


def test_show_introduction(capsys):
    cli_presenter.show_introduction()
    captured = capsys.readouterr()
    expected_output = "Welcome to NLTK-Me!\nWhat would you like to do?"
    assert captured.out == expected_output


def test_show_options(monkeypatch):
    monkeypatch.setattr("sys.stdin", "2")
    selected_option = cli_presenter.show_options()
    assert selected_option == "2"

