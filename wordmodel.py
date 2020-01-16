from sentence import SentenceModel
# View Model Class that holds Words. 
class WordModel:

    def __init__(self, word, document, total_occurences, sentence):
        self.word = word
        self.document = document 
        self.total_occurences = total_occurences
        self.sentence = sentence
        

    def display(self):
        print(self.word, self.document, self.total_occurences)
        
    
    def get_sentence(self):
        return self.sentence

    def get_occurences(self):
        return self.total_occurences

    def get_word(self):
        return self.word

    def get_document(self):
        return self.document

    #MODEL: Word, Documents, Total Occurences, Sentences[]     
        