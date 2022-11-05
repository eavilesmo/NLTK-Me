class FileHandler:

    def readFile(self, get_file_text):
        return open(get_file_text, encoding="UTF-8").read()

    def write(self, filename_path, tokenized_text):
        with open(filename_path, "w") as result_text:
            for line in tokenized_text:
                result_text.write(line)
                result_text.write("\n")

    def writeStopwords(self, filename_path, tokenized_file, stop_words, stopword_symbols):
        with open(filename_path, "w") as result_stopwords:
            for word in tokenized_file:
                word = word.lower()
                if word not in stop_words and word not in stopword_symbols:
                    result_stopwords.write(" " + word)
