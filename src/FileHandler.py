class FileHandler:

    def read(self, get_file_text):
        return open(get_file_text, encoding="UTF-8").read()

    def write(self, filename_path, tokenized_text):
        with open(filename_path, "w") as result_text:
            for line in tokenized_text:
                result_text.write(line)
                result_text.write("\n")
