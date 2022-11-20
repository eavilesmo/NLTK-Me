from nltk.tokenize import sent_tokenize
from nltk import word_tokenize
from nltk.tokenize.treebank import TreebankWordTokenizer
from nltk import FreqDist
from nltk.corpus import stopwords

from src.domain.SymbolCollection import symbols
from src.infrastructure.FileHandler import FileHandler


class NaturalLanguageToolkit:

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
            if word not in stop_words and word not in symbols:
                processed_content.append(word)
        return processed_content

    def count_total_words(self, content_to_process):
        tokenized_content = word_tokenize(content_to_process)
        total_words = len(tokenized_content)
        return total_words

    def count_repetitions_of_a_word(self, content_to_process, word_to_search_for):
        processed_content = content_to_process.lower()
        tokenizer = TreebankWordTokenizer()
        tokenized_content = tokenizer.tokenize(processed_content)
        frequency_distributor = FreqDist(tokenized_content)
        word_to_search_for = word_to_search_for.lower()
        number_of_repetitions = frequency_distributor[word_to_search_for]
        return number_of_repetitions

    def find_most_repeated_word(self, content_to_process):
        tokenizer = TreebankWordTokenizer()
        tokenized_content = tokenizer.tokenize(content_to_process)
        frequency_distributor = FreqDist(tokenized_content)
        most_repeated_word = frequency_distributor.max()
        return most_repeated_word
