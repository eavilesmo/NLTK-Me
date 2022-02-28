# -----------------------------------------------------------------------------
# Description of the file
# -----------------------------------------------------------------------------

# The Text_Processing_Tools file allocates all the functions needed for the
# Main program.

# -----------------------------------------------------------------------------
# Imports
# -----------------------------------------------------------------------------

from nltk.tokenize import sent_tokenize
from nltk import word_tokenize
from nltk.tokenize.treebank import TreebankWordTokenizer
from nltk import FreqDist
from nltk.corpus import stopwords
from GUI_Constants import *
import os

# -----------------------------------------------------------------------------
# Classes
# -----------------------------------------------------------------------------


# Class Error for handling errors of the application
class ErrorCode:
    UNICODE_ERROR = 1
    VALUE_ERROR = 2
    PATH_ERROR = 3
    EMPTY_FILE_ERROR = 4
    NO_ERROR = 5

# -----------------------------------------------------------------------------
# Lists
# -----------------------------------------------------------------------------


stopword_symbols = ["¡", "!", ",", ".", ";", "-", "_", "¿", "?", "(", ")",
                    "/", "\\", "@", "#", ":", "'", "’"]

# -----------------------------------------------------------------------------
# Functions
# -----------------------------------------------------------------------------


# Text tokenizer - Divides a text into sentences
def tokenize_text(get_file_text, filename_path):
    try:
        file_for_tok_text = open(get_file_text).read()
        tokenized_text = sent_tokenize(file_for_tok_text)
        if len(tokenized_text) <= 0:
            return ErrorCode.EMPTY_FILE_ERROR
        else:
            with open(filename_path, "w") as result_text:
                for line in tokenized_text:
                    result_text.write(line)
                    result_text.write("\n")
            return ErrorCode.NO_ERROR
    except FileNotFoundError:
        return ErrorCode.PATH_ERROR


# Sentence tokenizer - Divides one or more sentences into words
def tokenize_sentence(get_file_sentence, filename_path):
    try:
        file_for_tok_sentence = open(get_file_sentence).read()
        tokenized_sentence = word_tokenize(file_for_tok_sentence)
        if len(tokenized_sentence) <= 0:
            return ErrorCode.EMPTY_FILE_ERROR
        else:
            with open(filename_path, "w") as result_sentence:
                for word in tokenized_sentence:
                    result_sentence.write(word)
                    result_sentence.write("\n")
            return ErrorCode.NO_ERROR
    except FileNotFoundError:
        return ErrorCode.PATH_ERROR
    except UnicodeDecodeError:
        return ErrorCode.UNICODE_ERROR


# Stopwords remover - Removes the stopwords from a text
def stopwords_remover(get_file_stopwords, filename_path, stopwords_language):
    try:
        file_for_stopwords_remover = open(get_file_stopwords).read()
        stop_words = set(stopwords.words(stopwords_language))
        tokenized_file = word_tokenize(file_for_stopwords_remover)
        if len(tokenized_file) <= 0:
            return ErrorCode.EMPTY_FILE_ERROR
        with open(filename_path, "w") as result_stopwords:
            for word in tokenized_file:
                word = word.lower()
                if word not in stop_words and word not in stopword_symbols:
                    result_stopwords.write(" " + word)
        return ErrorCode.NO_ERROR
    except FileNotFoundError:
        return ErrorCode.PATH_ERROR
    except UnicodeDecodeError:
        return ErrorCode.UNICODE_ERROR


# Total words - Shows how many words are in the text
def total_words_count(get_file_twords):
    try:
        file_for_twords = open(get_file_twords).read()
        if len(file_for_twords) <= 0:
            data_from_twords = 0
            return ErrorCode.EMPTY_FILE_ERROR, data_from_twords
        tokenized_sentence = word_tokenize(file_for_twords)
        data_from_twords = len(tokenized_sentence)
        return ErrorCode.NO_ERROR, data_from_twords
    except FileNotFoundError:
        data_from_twords = 0
        return ErrorCode.PATH_ERROR, data_from_twords
    except UnicodeDecodeError:
        data_from_twords = 0
        return ErrorCode.UNICODE_ERROR, data_from_twords


# Frequency Distribution functions
# FreqDist Count - Count how many times a certain word appears in the text
def freqdist_count(get_file_fdist_count, get_data_count):
    try:
        file_for_fdist_count = open(get_file_fdist_count).read()
        file_for_fdist_count = file_for_fdist_count.lower()
        tokenizer = TreebankWordTokenizer()
        fdist_count_tokenized = tokenizer.tokenize(file_for_fdist_count)
        if len(fdist_count_tokenized) <= 0:
            data_from_count = 0
            return ErrorCode.EMPTY_FILE_ERROR, data_from_count
        fdist_count = FreqDist(fdist_count_tokenized)
        get_data_count = get_data_count.lower()
        data_from_count = fdist_count[get_data_count]
        return ErrorCode.NO_ERROR, data_from_count
    except FileNotFoundError:
        data_from_count = 0
        return ErrorCode.PATH_ERROR, data_from_count
    except UnicodeDecodeError:
        data_from_count = 0
        return ErrorCode.UNICODE_ERROR, data_from_count


# FreqDist Max - Shows most repeated word
def freqdist_max(get_file_fdist_max):
    try:
        file_for_fdist_max = open(get_file_fdist_max).read()
        tokenizer = TreebankWordTokenizer()
        fdist_max_tokenized = tokenizer.tokenize(file_for_fdist_max)
        if len(fdist_max_tokenized) <= 0:
            data_from_max = 0
            return ErrorCode.EMPTY_FILE_ERROR, data_from_max
        fdist_max = FreqDist(fdist_max_tokenized)
        data_from_max = fdist_max.max()
        return ErrorCode.NO_ERROR, data_from_max
    except FileNotFoundError:
        data_from_max = 0
        return ErrorCode.PATH_ERROR, data_from_max
    except UnicodeDecodeError:
        data_from_max = 0
        return ErrorCode.UNICODE_ERROR, data_from_max


# FreqDist Plot - Shows a graph with words frequency
def freqdist_plot(get_file_fdist_plot, get_data_plot):
    try:
        file_for_fdist_plot = open(get_file_fdist_plot, encoding="UTF-8").read()
        tokenizer = TreebankWordTokenizer()
        fdist_plot_tokenized = tokenizer.tokenize(file_for_fdist_plot)
        if len(fdist_plot_tokenized) <= 0:
            data_from_plot = 0
            return ErrorCode.EMPTY_FILE_ERROR, data_from_plot
        fdist_plot = FreqDist(fdist_plot_tokenized)
        data_from_plot = fdist_plot.plot(int(get_data_plot))
        return ErrorCode.NO_ERROR, data_from_plot
    except FileNotFoundError:
        data_from_plot = 0
        return ErrorCode.PATH_ERROR, data_from_plot
    except UnicodeDecodeError:
        data_from_plot = 0
        return ErrorCode.UNICODE_ERROR, data_from_plot
