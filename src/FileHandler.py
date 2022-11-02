class FileHandler:

    def read(self, get_file_text):
        return open(get_file_text, encoding="UTF-8").read()
