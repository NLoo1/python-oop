from wordfinder import WordFinder

class SpecialWordFinder(WordFinder):

    def __init__(self, file_path):
        super().__init__(file_path)

    def __repr__(self):
        return f"SpecialWordFinder {self.file_path}"
    
    def read_file(self):
        super().read_file()
        for line in self.word_list:
            if(line[0] == "#" or line.isspace()):
                self.word_list.pop(self.word_list.index(line))
        return self.word_list

    def random(self):
        super().random()