import PySimpleGUI as sg
from PySimpleGUI import Column, Frame
from src.GUI_Constants import *
from src.infrastructure.Executor import Executor


def create_welcome_layout():
    welcome_layout = [[sg.Text(WELCOME_TEXT_EN)],
                      [sg.Text(WELCOME_TEXT_ES)],
                      [sg.Button(ENG_BUT, key=ENG_BUT_KEY),
                       sg.Button(SPA_BUT, key=SPA_BUT_KEY)]]
    return welcome_layout


def create_main_layout(language):
    col1 = Column([
        [sg.Text(language["general_description"])],
        [Frame(language["select_file_frame"], [
            [sg.Text(language["text_browse"], size=SIZE_TEXT_L,
                     key=KEY_TEXT_BROWSE),
             sg.FileBrowse(language["button_browse"], enable_events=True,
                           key=KEY_BROWSE, file_types=FILE_TYPES,
                           size=SIZE_BUTTON, target=KEY_BROWSE)]])],
        [Frame(language["choose_option_frame"], [
            [sg.Radio(language["button_tok_text"], "RADIO01",
                      enable_events=True, key=KEY_TOK_TEXT)],
            [sg.Radio(language["button_tok_sent"], "RADIO01",
                      enable_events=True, key=KEY_TOK_SENT)],
            [sg.Radio(language["button_stopwords"], "RADIO01",
                      enable_events=True, key=KEY_STOPWORDS)],
            [sg.pin(sg.Text(language["stopwords_lang_description"],
                            key=KEY_STOPWORDS_TEXT, visible=False))],
            [sg.pin(sg.Radio(language["button_stopwords_lang1"], "RADIO02",
                             enable_events=True, key=KEY_STOPWORDS_BUT1,
                             visible=False, pad=(30, 0), size=SIZE_TEXT_S)),
             sg.pin(sg.Radio(language["button_stopwords_lang2"], "RADIO02",
                             enable_events=True, key=KEY_STOPWORDS_BUT2,
                             visible=False, pad=(30, 0), size=SIZE_TEXT_S))],
            [sg.Radio(language["button_total_words"], "RADIO01",
                      enable_events=True, key=KEY_TOTAL_WORDS)],
            [sg.Radio(language["button_count"], "RADIO01", enable_events=True,
                      key=KEY_COUNT)],
            [sg.pin(sg.Text(language["count_var_description"],
                            key=KEY_COUNT_TEXT, visible=False)),
             sg.pin(sg.InputText(key=KEY_COUNT_INPUT, enable_events=True,
                                 visible=False, size=SIZE_TEXT_S))],
            [sg.Radio(language["button_max"], "RADIO01", enable_events=True,
                      key=KEY_MAX)],
            [sg.Radio(language["button_plot"], "RADIO01", enable_events=True,
                      key=KEY_PLOT)],
            [sg.pin(sg.Text(language["plot_var_description"],
                            key=KEY_PLOT_TEXT, visible=False)),
             sg.pin(sg.InputText(key=KEY_PLOT_INPUT, enable_events=True,
                                 visible=False, size=SIZE_TEXT_S))]])],
        [Frame(language["save_as_frame"], [
            [sg.Text(language["text_save_as"], size=SIZE_TEXT_L,
                     key=KEY_TEXT_SAVE_AS),
             sg.FileSaveAs(language["button_save_as"], key=KEY_SAVE_AS,
                           file_types=FILE_TYPES, size=SIZE_BUTTON,
                           disabled=True, target=KEY_SAVE_AS,
                           enable_events=True)]])],
        [sg.OK(language["button_ok"], key=KEY_OK, disabled=True)]])

    col2 = Column([
        [Frame(language["information_frame"],
               [[sg.Text(language["info_frame_description"],
                         key=KEY_INFORMATION, size=SIZE_INFORMATION)]])]])
    return col1, col2


def error_handling(error_result, language, key, function_result="None"):
    if error_result == 1:
        sg.Popup(language["unicode_error"], title=TITLE_WIN)
    if error_result == 2:
        sg.Popup(language["value_error"], title=TITLE_WIN)
    if error_result == 3:
        sg.Popup(language["path_error"], title=TITLE_WIN)
    if error_result == 4:
        sg.Popup(language["empty_file_error"], title=TITLE_WIN)
    elif error_result == 5:
        if key == "tokenize":
            sg.Popup(language["popup_tok"], title=TITLE_WIN)
        if key == "stopwords":
            sg.Popup(language["popup_stopwords"], title=TITLE_WIN)
        if key == "count":
            sg.Popup(language["popup_count"].format(function_result), title=TITLE_WIN)
        if key == "total_words":
            sg.Popup(language["popup_total_words"].format(function_result), title=TITLE_WIN)
        if key == "max":
            sg.Popup(language["popup_max"].format(function_result), title=TITLE_WIN)
        if key == "plot":
            pass


def main():
    sg.theme(SG_THEME)

    welcome_layout = create_welcome_layout()
    welcome_window = sg.Window(TITLE_WIN, welcome_layout)

    while True:
        event, values = welcome_window.read()
        if event == sg.WIN_CLOSED:
            break
        if event == ENG_BUT_KEY:
            language = dict_EN
            welcome_window.close()
        if event == SPA_BUT_KEY:
            language = dict_ES
            welcome_window.close()

    col1, col2 = create_main_layout(language)
    main_layout = [[col1, col2]]
    main_window = sg.Window(TITLE_WIN, main_layout)

    while True:
        event, values = main_window.read()
        if event == sg.WIN_CLOSED:
            break

        main_window[KEY_OK].update(disabled=True)
        main_window[KEY_SAVE_AS].update(disabled=True)

        executor = Executor()

        if values[KEY_BROWSE]:
            if values[KEY_TOK_TEXT]:
                main_window[KEY_SAVE_AS].update(disabled=False)
                if values[KEY_SAVE_AS]:
                    main_window[KEY_OK].update(disabled=False)
                    if event == KEY_OK:
                        get_file_text = values[KEY_BROWSE]
                        filename_path = values[KEY_SAVE_AS]
                        error_result = executor.tokenize_text(get_file_text, filename_path)
                        key = "tokenize"
                        error_handling(error_result, language, key)
            elif values[KEY_TOK_SENT]:
                main_window[KEY_SAVE_AS].update(disabled=False)
                if values[KEY_SAVE_AS]:
                    main_window[KEY_OK].update(disabled=False)
                    if event == KEY_OK:
                        get_file_sentence = values[KEY_BROWSE]
                        filename_path = values[KEY_SAVE_AS]
                        error_result = executor.tokenize_sentence(get_file_sentence, filename_path)
                        key = "tokenize"
                        error_handling(error_result, language, key)
            elif values[KEY_STOPWORDS]:
                main_window[KEY_SAVE_AS].update(disabled=False)
                if values[KEY_STOPWORDS_BUT1] or values[KEY_STOPWORDS_BUT2]:
                    if values[KEY_SAVE_AS]:
                        main_window[KEY_OK].update(disabled=False)
                    if event == KEY_OK:
                        get_file_stopwords = values[KEY_BROWSE]
                        filename_path = values[KEY_SAVE_AS]
                        stopwords_language = ""
                        if values[KEY_STOPWORDS_BUT1]:
                            stopwords_language = "english"
                        elif values[KEY_STOPWORDS_BUT2]:
                            stopwords_language = "spanish"
                        error_result = executor.remove_stopwords(get_file_stopwords, filename_path, stopwords_language)
                        key = "stopwords"
                        error_handling(error_result, language, key)
            elif values[KEY_TOTAL_WORDS]:
                main_window[KEY_OK].update(disabled=False)
                if event == KEY_OK:
                    get_file_twords = values[KEY_BROWSE]
                    error_result, function_result = executor.count_total_words(get_file_twords)
                    key = "total_words"
                    error_handling(error_result, language, key,
                                   function_result)
            elif values[KEY_COUNT]:
                if values[KEY_COUNT_INPUT]:
                    main_window[KEY_OK].update(disabled=False)
                    if event == KEY_OK:
                        get_file_fdist_count = values[KEY_BROWSE]
                        get_data_count = values[KEY_COUNT_INPUT]
                        error_result, function_result = executor.count_repetitions_of_a_word(get_file_fdist_count, get_data_count)
                        key = "count"
                        error_handling(error_result, language, key, function_result)
            elif values[KEY_MAX]:
                main_window[KEY_OK].update(disabled=False)
                if event == KEY_OK:
                    get_file_fdist_max = values[KEY_BROWSE]
                    error_result, function_result = executor.find_most_repeated_word(get_file_fdist_max)
                    key = "max"
                    error_handling(error_result, language, key, function_result)

        if event == KEY_BROWSE:
            main_window[KEY_TEXT_BROWSE].update(values[KEY_BROWSE])

        if event == KEY_TOK_TEXT:
            main_window[KEY_INFORMATION].update(
                language["tok_text_description"])

        if event == KEY_TOK_SENT:
            main_window[KEY_INFORMATION].update(
                language["tok_sentence_description"])

        if event == KEY_STOPWORDS:
            main_window[KEY_INFORMATION].update(
                language["stopwords_rem_description"])
            main_window[KEY_STOPWORDS_TEXT].update(visible=True)
            main_window[KEY_STOPWORDS_BUT1].update(visible=True)
            main_window[KEY_STOPWORDS_BUT2].update(visible=True)

        if event != KEY_STOPWORDS and event != KEY_OK and event != KEY_STOPWORDS_BUT1 and event != KEY_STOPWORDS_BUT2\
                and event != KEY_BROWSE and event != KEY_SAVE_AS:
            main_window[KEY_STOPWORDS_TEXT].update(visible=False)
            main_window[KEY_STOPWORDS_BUT1].update(visible=False)
            main_window[KEY_STOPWORDS_BUT2].update(visible=False)

        if event == KEY_TOTAL_WORDS:
            main_window[KEY_INFORMATION].update(language["twords_description"])

        if event == KEY_COUNT:
            main_window[KEY_INFORMATION].update(language["count_description"])
            main_window[KEY_COUNT_TEXT].update(visible=True)
            main_window[KEY_COUNT_INPUT].update(visible=True)

        if event != KEY_COUNT and event != KEY_OK and event != KEY_COUNT_INPUT and event != KEY_BROWSE:
            main_window[KEY_COUNT_TEXT].update(visible=False)
            main_window[KEY_COUNT_INPUT].update(visible=False)

        if event == KEY_MAX:
            main_window[KEY_INFORMATION].update(language["max_description"])

        if event == KEY_PLOT:
            main_window[KEY_INFORMATION].update(language["plot_description"])
            main_window[KEY_PLOT_TEXT].update(visible=True)
            main_window[KEY_PLOT_INPUT].update(visible=True)

        if event != KEY_PLOT and event != KEY_OK and event != KEY_PLOT_INPUT and event != KEY_BROWSE:
            main_window[KEY_PLOT_TEXT].update(visible=False)
            main_window[KEY_PLOT_INPUT].update(visible=False)

        if event == KEY_SAVE_AS:
            main_window[KEY_TEXT_SAVE_AS].update(values[KEY_SAVE_AS])


if __name__ == "__main__":
    main()
