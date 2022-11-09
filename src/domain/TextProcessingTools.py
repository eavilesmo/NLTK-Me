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

    def tokenize_sentence(self, content_to_tokenize):
        return word_tokenize(content_to_tokenize)

    def remove_stopwords(self, content_to_process, language):
        stop_words = set(stopwords.words(language))
        tokenized_file = word_tokenize(content_to_process)
        processed_content = []
        for word in tokenized_file:
            word = word.lower()
            if word not in stop_words and word not in stopword_symbols:
                processed_content.append(word)
        return processed_content

    def total_words_count(self, content_to_process):
        tokenized_content = word_tokenize(content_to_process)
        total_words = len(tokenized_content)
        return total_words

    def freqdist_count(self, content_to_process, word_to_search_for):
        processed_content = content_to_process.lower()
        tokenizer = TreebankWordTokenizer()
        tokenized_content = tokenizer.tokenize(processed_content)
        processed_tokenized_content = FreqDist(tokenized_content)
        word_to_search_for = word_to_search_for.lower()
        number_of_repetitions = processed_tokenized_content[word_to_search_for]
        return number_of_repetitions

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
