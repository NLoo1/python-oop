"""Word Finder: finds random words from a dictionary."""

from random import randint

class WordFinder:
    ...
    def __init__(self, file_path):
        self.file_path = file_path
        self.word_list = self.read_file()

    def __repr__(self):
        return f"WordFinder: {self.file_path}"
    
    def read_file(self):
        word_list = []
        file = open(self.file_path)
        for line in file:
            new_word = line.split("\n")[0]
            word_list.append(new_word)
        file.close()
        return word_list

    def random(self):
        random_int = randint(0, len(self.word_list)-1)
        return self.word_list[random_int]

