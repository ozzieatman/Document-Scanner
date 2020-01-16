# View Model Class that holds Sentence

class SentenceModel:
    # Sentence: Word Pos, Doc, Line Number
    # I don't have time for Philosophy (Line Number, Words to Bold, Document)
    def __init__(self, lString, doc, line_number):
        self.line_string = lString
        self.doc = doc
        self.line_number = line_number

    def get_line(self):
        return self.line_string

    def get_index(self):
        return self.line_number
