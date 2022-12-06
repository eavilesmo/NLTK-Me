from nltk.tokenize import sent_tokenize as sentence_tokenizer
from nltk import word_tokenize as word_tokenizer
from nltk.tokenize.treebank import TreebankWordTokenizer
from nltk import FreqDist
from nltk.corpus import stopwords

from src.domain.PunctuationMarkCollection import punctuation_mark_collection


class NaturalLanguageToolkit:

    def tokenize_text(self, content_to_process):
        return sentence_tokenizer(content_to_process)

    def tokenize_sentence(self, content_to_process):
        return word_tokenizer(content_to_process)

    def remove_stopwords(self, content_to_process, language):
        stopword_collection = set(stopwords.words(language))
        tokenized_content = word_tokenizer(content_to_process)
        output_content = []
        for word in tokenized_content:
            word = word.lower()
            if word not in stopword_collection and word not in punctuation_mark_collection:
                output_content.append(word)
        return output_content

    def count_total_words(self, content_to_process):
        tokenized_content = word_tokenizer(content_to_process)
        total_words = len(tokenized_content)
        return total_words

    def count_repetitions_of_a_word(self, content_to_process, word_to_search_for):
        tokenizer = TreebankWordTokenizer()
        tokenized_content = tokenizer.tokenize(content_to_process.lower())
        frequency_distributor = FreqDist(tokenized_content)
        number_of_repetitions = frequency_distributor[word_to_search_for.lower()]
        return number_of_repetitions

    def find_most_repeated_word(self, content_to_process):
        tokenizer = TreebankWordTokenizer()
        tokenized_content = tokenizer.tokenize(content_to_process)
        frequency_distributor = FreqDist(tokenized_content)
        most_repeated_word = frequency_distributor.max()
        return most_repeated_word
