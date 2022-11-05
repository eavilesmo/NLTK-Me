from nltk.tokenize import sent_tokenize
from nltk import word_tokenize
from nltk.tokenize.treebank import TreebankWordTokenizer
from nltk import FreqDist
from nltk.corpus import stopwords

from src.ErrorCode import ErrorCode
from src.FileHandler import FileHandler

stopword_symbols = ["¡", "!", ",", ".", ";", "-", "_", "¿", "?", "(", ")",
                    "/", "\\", "@", "#", ":", "'", "’"]


class TextProcessingTools:
    def __init__(self, file_handler: FileHandler):
        self.file_handler = file_handler

    def tokenize_text(self, get_file_text, filename_path):
        try:
            file_for_tok_text = self.file_handler.readFile(get_file_text)
            tokenized_text = sent_tokenize(file_for_tok_text)
            if len(tokenized_text) <= 0:
                return ErrorCode.EMPTY_FILE_ERROR
            else:
                self.file_handler.write(filename_path, tokenized_text)
                return tokenized_text
        except FileNotFoundError:
            return "File not found"

    def tokenize_sentence(self, get_file_sentence, filename_path):
        try:
            file_for_tok_sentence = self.file_handler.readFile(get_file_sentence)
            tokenized_sentence = word_tokenize(file_for_tok_sentence)
            if len(tokenized_sentence) <= 0:
                return ErrorCode.EMPTY_FILE_ERROR
            else:
                self.file_handler.write(filename_path, tokenized_sentence)
                return tokenized_sentence
        except FileNotFoundError:
            return ErrorCode.PATH_ERROR
        except UnicodeDecodeError:
            return ErrorCode.UNICODE_ERROR

    def stopwords_remover(self, get_file_stopwords, filename_path, stopwords_language):
        try:
            file_for_stopwords_remover = open(get_file_stopwords, encoding="UTF-8").read()
            stop_words = set(stopwords.words(stopwords_language))
            tokenized_file = word_tokenize(file_for_stopwords_remover)
            if len(tokenized_file) <= 0:
                return ErrorCode.EMPTY_FILE_ERROR
            with open(filename_path, "w") as result_stopwords:
                for word in tokenized_file:
                    word = word.lower()
                    if word not in stop_words and word not in stopword_symbols:
                        result_stopwords.write(" " + word)
            return tokenized_file
        except FileNotFoundError:
            return ErrorCode.PATH_ERROR
        except UnicodeDecodeError:
            return ErrorCode.UNICODE_ERROR

    def total_words_count(get_file_twords):
        """Total words - Shows how many words are in the text"""
        try:
            file_for_twords = open(get_file_twords, encoding="UTF-8").read()
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
    def freqdist_count(get_file_fdist_count, get_data_count):
        """
        FreqDist Count - Count how many times a certain word appears in the text
        """
        try:
            file_for_fdist_count = open(get_file_fdist_count, encoding="UTF-8").read()
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

    def freqdist_max(get_file_fdist_max):
        """FreqDist Max - Shows most repeated word"""
        try:
            file_for_fdist_max = open(get_file_fdist_max, encoding="UTF-8").read()
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

    def freqdist_plot(get_file_fdist_plot, get_data_plot):
        """FreqDist Plot - Shows a graph with words frequency"""
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
