from wordfinder import WordFinder

class SpecialWordFinder(WordFinder):

    def __init__(self, file_path):
        super().__init__(file_path)
        self.word_list = self.read_file()

    def __repr__(self):
        return f"SpecialWordFinder {self.file_path}"
    
    def read_file(self):
        unfiltered_list = super().read_file()
        for line in unfiltered_list:
            if("#" in line):
                unfiltered_list.remove(line)
        filtered_list = [x for x in unfiltered_list if x != ""]
        return filtered_list

    def random(self):
        return super().random()