# -----------------------------------------------------------------------------
# Description of the file
# -----------------------------------------------------------------------------

# The GUI_Constants file contains all the constants, variables and
# dictionaries needed for the GUI.

# -----------------------------------------------------------------------------

# Miscellaneous
SG_THEME = "LightBlue3"
TITLE_WIN = "NLTK-Me!"
WELCOME_TEXT_EN = "Hello! Welcome to NLTK-Me!\n" \
                  "Which language would you like to choose?"
WELCOME_TEXT_ES = "¡Hola! Te damos la bienvenida a NLTK-Me!\n" \
                  "¿Qué idioma quieres escoger?"
ENG_BUT = "English"
ENG_BUT_KEY = "EN_lang"
SPA_BUT = "Español"
SPA_BUT_KEY = "ES_lang"

# Size of elements
SIZE_BUTTON = (6, 1)
SIZE_TEXT_L = (34, 1)
SIZE_TEXT_S = (6, 2)
SIZE_INFORMATION = (25, 17)

# Key names for the elements
KEY_BROWSE = "browse"
KEY_TEXT_BROWSE = "text_browse"
FILE_TYPES = (("Text Files", "*.txt"),)
KEY_TOK_TEXT = "tok_text"
KEY_TOK_SENT = "tok_sentence"
KEY_STOPWORDS = "stopwords"
KEY_STOPWORDS_TEXT = "stopwords_text"
KEY_STOPWORDS_BUT1 = "stopwords_but1"
KEY_STOPWORDS_BUT2 = "stopwords_but2"
KEY_TOTAL_WORDS = "total_words"
KEY_COUNT = "fdist01"
KEY_COUNT_TEXT = "fdist01_text"
KEY_COUNT_INPUT = "fdist01_input"
KEY_MAX = "fdist02"
KEY_PLOT = "fdist03"
KEY_PLOT_TEXT = "fdist03_text"
KEY_PLOT_INPUT = "fdist03_input"
KEY_SAVE_AS = "save_file"
KEY_TEXT_SAVE_AS = "text_save_as"
KEY_OK = "OK"
KEY_INFORMATION = "information"


# Dictionary for making the GUI bilingual
dict_EN = {
    # Descriptions
    "general_description": "Welcome to NLTK-Me!\nThis is a program based "
                           "on the NLTK library for Python.",
    "info_frame_description": "When you click on an option from the list, you "
                              "will see here general information about it.",
    "text_browse": "Please select a file to work with",
    "tok_text_description": "With Text Tokenizer, you can tokenize (split) "
                            "a text into sentences. The text is split based "
                            "on full stops.\nThis option will create a file "
                            "with the result. You can choose the path and the "
                            "name for your file with the button "
                            "'Save as'.",
    "tok_sentence_description": "With Sentence Tokenizer, you can tokenize "
                                "(split) a sentence into words. The sentences "
                                "are split based on spaces.\nThis option will "
                                "create a file with the result. You can "
                                "choose the path and the name for your file "
                                "with the button 'Save as'.",
    "stopwords_rem_description": "This function removes the stopwords from a "
                                 "text. This means that all words with no "
                                 "meaning in the text (as articles, "
                                 "prepositions or punctuation marks) will be "
                                 "removed from the text.\nThis option will "
                                 "create a file with the result. You can "
                                 "choose the path and the name for your "
                                 "file with the button 'Save as'.",
    "twords_description": "This function shows how many words are in the text."
                          "\nA popup window will appear with the result.",
    "count_description": "This function shows how many times a word appears "
                         "in the text.\nA popup window will appear with "
                         "the result.\nPlease note this function isn't case"
                         "sensitive, which means that it differentiate between"
                         " capital or lower-case letters.",
    "count_var_description": "Enter the word you want to count:",
    "max_description": "This function shows the most common word in the text."
                       "\nA popup window will appear with the result.\nIt's "
                       "recommended to first execute the function 'Remove "
                       "stopwords' in the file to avoid getting strange "
                       "results (for instance, getting articles, pronouns "
                       "or even punctuation marks as the most frequent word.)",
    "plot_description": "This function shows a graph with the most frequent "
                        "words in the text and the number of time they appear. "
                        "You can choose how many words will be displayed.\nA"
                        " new window will appear with the graph.\nIt's "
                        "recommended to first execute the function 'Remove "
                        "stopwords' in the file to avoid getting strange "
                        "results (for instance, getting articles, pronouns or "
                        "even punctuation marks as words in the graph.)",
    "plot_var_description": "No. of words displayed in the graph:",
    "stopwords_lang": "english",
    "popup_tok": "Your text has been tokenized!",
    "popup_stopwords": "The stopwords have been removed from your text!",
    "popup_total_words": "The total number of words in the text is {}",
    "popup_count": "This word appears {} times",
    "popup_max": "The most repeated word in the text is {} ",
    "text_save_as": "Please choose a path to save your file",
    "stopwords_lang_description": "Please select the language of your text:",

    # Errors
    "unicode_error": "The program is not able to work with your file due "
                     "to its encoding.\nPlease change the encoding of your "
                     "file before trying again.",
    "value_error": "The introduced value is not correct. Please try again.",
    "path_error": "The path you introduced is not correct. Please try again.",
    "empty_file_error": "The file you introduced is empty! Please try again.",

    # Frames
    "information_frame": "Information",
    "select_file_frame": "Select your file",
    "choose_option_frame": "What would you like to do?",
    "save_as_frame": "Save your file",

    # Buttons
    "button_browse": "Browse",
    "button_ok": "Go!",
    "button_tok_text": "Tokenize a text",
    "button_tok_sent": "Tokenize a sentence",
    "button_stopwords": "Remove the stopwords",
    "button_stopwords_lang1": "English",
    "button_stopwords_lang2": "Spanish",
    "button_total_words": "Count total words in a text",
    "button_count": "Count frequency of words in a text",
    "button_max": "Show the most frequent word in a text",
    "button_plot": "Show a graph with the frequency of words",
    "button_save_as": "Save as"
}

dict_ES = {
    # Descriptions
    "general_description": "¡Bienvenido/a a NLTK-Me!\nUn programa basado en "
                           "la librería NLTK para Python.",
    "info_frame_description": "Cuando hagas clic sobre una opción, aquí verás "
                              "información general sobre ella.",
    "text_browse": "Selecciona con qué archivo quieres trabajar",
    "tok_text_description": "Con el Tokenizador de texto, puedes tokenizar "
                            "(segmentar) un texto en frases. Los puntos de "
                            "cada frase indicarán al programa dónde segmentar "
                            "el texto.\nEsta opción guardará los resultados "
                            "en un archivo. Puedes escoger la ruta y el "
                            "nombre del archivo con el botón 'Guardar'.",
    "tok_sentence_description": "Con el Tokenizador de frases, puedes "
                                "tokenizar (segmentar) una frase en palabras. "
                                "Los espacios entre palabra y palabra "
                                "indicarán al programa dónde segmentar la "
                                "frase.\nEsta opción guardará los resultados "
                                "en un archivo. Puedes escoger la ruta y el "
                                "nombre del archivo con el botón 'Guardar'.",
    "stopwords_rem_description": "Esta opción quita las stopwords de un "
                                 "texto. Esto significa que se quitarán todas "
                                 "las palabras sin significado del texto "
                                 "(como artículos, preposiciones o signos de "
                                 "puntuación).\n Esta opción guardará los "
                                 "resultados en un archivo. Puedes escoger "
                                 "la ruta y el nombre del archivo con el "
                                 "botón 'Guardar'.",
    "twords_description": "Esta función muestra cuántas palabras en total hay "
                          "en un texto.\nSe mostrará un popup con el "
                          "resultado.",
    "count_description": "Esta función muestra cuántas veces aparece una "
                         "palabra en un texto.\nSe mostrará un popup con el "
                         "resultado.\nTen en cuenta que esta función no "
                         "distingue entre mayúsculas y minúsculas.",
    "count_var_description": "Introduce la palabra que quieras contar:",
    "max_description": "Esta función muestra la palabra más común en el texto."
                       "\nSe mostrará un popup con el resultado.\nSe "
                       "recomienda ejecutar primero la función 'Quitar las "
                       "stopwords' en el mismo archivo para evitar que dé "
                       "lugar a resultados extraños (por ejemplo, que la "
                       "palabra más frecuente sea un artículo, un pronombre o "
                       "incluso un signo de puntuación.",
    "plot_description": "Esta función muestra un gráfico con las palabras más "
                        "frecuentes en el texto y el número de veces que "
                        "aparecen. Puedes escoger el número de palabras que "
                        "aparecerán en él.\nSe mostrará un popup con el "
                        "resultado.\nSe recomienda ejecutar primero la "
                        "función 'Quitar las stopwords' en el mismo archivo "
                        "para evitar que dé lugar a resultados extraños (por "
                        "ejemplo, que artículos, pronombres o signos de "
                        "puntuación aparezcan como palabras en el gráfico).",
    "plot_var_description": "Nº de palabras que se mostrarán en el gráfico:",
    "stopwords_lang": "spanish",
    "popup_tok": "¡Hemos tokenizado tu archivo!",
    "popup_stopwords": "¡Hemos quitado las stopwords de tu texto!",
    "popup_total_words": "El número total de palabras de este texto es {}",
    "popup_count": "Esta palabra aparece {} veces",
    "popup_max": "La palabra que más se repite en el texto es {}",
    "text_save_as": "Elige dónde guardar tu archivo",
    "stopwords_lang_description": "Selecciona el idioma de tu texto:",

    # Errors
    "unicode_error": "El programa no puede trabajar con tu archivo debido a "
                     "su codificación.\nCambia la codificación del archivo "
                     "antes de intentarlo de nuevo.",
    "value_error": "El valor introducido no es correcto. Inténtalo de nuevo.",
    "path_error": "La ruta introducida no es correcta. Inténtalo de nuevo.",
    "empty_file_error": "¡El archivo que has escogido está vacío! "
                        "Inténtalo de nuevo.",

    # Frames
    "information_frame": "Información",
    "select_file_frame": "Selecciona un archivo",
    "choose_option_frame": "¿Qué te gustaría hacer?",
    "save_as_frame": "Guarda tu archivo",

    # Buttons
    "button_browse": "Buscar",
    "button_ok": "¡Vamos!",
    "button_tok_text": "Tokenizar un texto",
    "button_tok_sent": "Tokenizar una frase",
    "button_stopwords": "Quitar las stopwords",
    "button_stopwords_lang1": "Inglés",
    "button_stopwords_lang2": "Español",
    "button_total_words": "Mostrar el número total de palabras en un texto",
    "button_count": "Mostrar la frecuencia de una palabra en un texto",
    "button_max": "Mostrar la palabra más frecuente en un texto",
    "button_plot": "Mostrar un gráfico con la frecuencia de las palabras "
                   "de un texto",
    "button_save_as": "Guardar"
}
