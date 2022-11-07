from nltk.tokenize import sent_tokenize
from nltk import word_tokenize
from nltk.tokenize.treebank import TreebankWordTokenizer
from nltk import FreqDist
from nltk.corpus import stopwords

from src.ErrorCode import ErrorCode
from src.infrastructure.FileHandler import FileHandler

stopword_symbols = ["¡", "!", ",", ".", ";", "-", "_", "¿", "?", "(", ")",
                    "/", "\\", "@", "#", ":", "'", "’"]


class TextProcessingTools:
    def __init__(self, file_handler: FileHandler):
        self.file_handler = file_handler

    def tokenize_text(self, content_to_tokenize):
        return sent_tokenize(content_to_tokenize)

    def tokenize_sentence(self, get_file_sentence, filename_path):
        try:
            file_for_tok_sentence = self.file_handler.read_file(get_file_sentence)
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
            file_for_stopwords_remover = self.file_handler.read_file(get_file_stopwords)
            stop_words = set(stopwords.words(stopwords_language))
            tokenized_file = word_tokenize(file_for_stopwords_remover)
            if len(tokenized_file) <= 0:
                return ErrorCode.EMPTY_FILE_ERROR
            result = []
            for word in tokenized_file:
                word = word.lower()
                if word not in stop_words and word not in stopword_symbols:
                    result.append(word)
            return result
        except FileNotFoundError:
            return ErrorCode.PATH_ERROR
        except UnicodeDecodeError:
            return ErrorCode.UNICODE_ERROR

    def total_words_count(self, get_file_twords):
        try:
            file_for_twords = self.file_handler.read_file(get_file_twords)
            if len(file_for_twords) <= 0:
                data_from_twords = 0
                return ErrorCode.EMPTY_FILE_ERROR, data_from_twords
            tokenized_sentence = word_tokenize(file_for_twords)
            data_from_twords = len(tokenized_sentence)
            return data_from_twords
        except FileNotFoundError:
            data_from_twords = 0
            return ErrorCode.PATH_ERROR, data_from_twords
        except UnicodeDecodeError:
            data_from_twords = 0
            return ErrorCode.UNICODE_ERROR, data_from_twords

    def freqdist_count(self, get_file_fdist_count, get_data_count):
        try:
            file_for_fdist_count = self.file_handler.read_file(get_file_fdist_count)
            file_for_fdist_count = file_for_fdist_count.lower()
            tokenizer = TreebankWordTokenizer()
            fdist_count_tokenized = tokenizer.tokenize(file_for_fdist_count)
            if len(fdist_count_tokenized) <= 0:
                data_from_count = 0
                return ErrorCode.EMPTY_FILE_ERROR, data_from_count
            fdist_count = FreqDist(fdist_count_tokenized)
            get_data_count = get_data_count.lower()
            data_from_count = fdist_count[get_data_count]
            return data_from_count
        except FileNotFoundError:
            data_from_count = 0
            return ErrorCode.PATH_ERROR, data_from_count
        except UnicodeDecodeError:
            data_from_count = 0
            return ErrorCode.UNICODE_ERROR, data_from_count

    def freqdist_max(self, get_file_fdist_max):
        try:
            file_for_fdist_max = self.file_handler.read_file(get_file_fdist_max)
            tokenizer = TreebankWordTokenizer()
            fdist_max_tokenized = tokenizer.tokenize(file_for_fdist_max)
            if len(fdist_max_tokenized) <= 0:
                data_from_max = 0
                return ErrorCode.EMPTY_FILE_ERROR, data_from_max
            fdist_max = FreqDist(fdist_max_tokenized)
            data_from_max = fdist_max.max()
            return data_from_max
        except FileNotFoundError:
            data_from_max = 0
            return ErrorCode.PATH_ERROR, data_from_max
        except UnicodeDecodeError:
            data_from_max = 0
            return ErrorCode.UNICODE_ERROR, data_from_max
