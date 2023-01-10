class FileHandler:

    def read(self, input_file):
        try:
            return open(input_file, encoding="UTF-8").read()
        except FileNotFoundError:
            return ""

    def write(self, file_path, processed_content):
        with open(file_path, "w") as output_file:
            for line in processed_content:
                output_file.write(line)
                output_file.write("\n")

    def write_stopwords(self, file_path, processed_content, stopwords, symbols):
        with open(file_path, "w") as output_file:
            for word in processed_content:
                word = word.lower()
                if word not in stopwords and word not in symbols:
                    output_file.write(" " + word)
