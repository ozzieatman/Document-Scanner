import api
from wordmodel import WordModel

class DocumentScanner:

    #Constructor: Takes list of Document Strings and build multiple models or "tables" reminiscient of a database table. 
    def __init__(self, document):
        self.document = document
        self.models = []

        for d in document:
            file_string = api.get_string_from_file(open(d, "rt"))
            dictionary = api.create_dictionary(file_string)
            ranked_dict = api.rank_dictionary(dictionary, file_string)
            model = api.build_model(ranked_dict, file_string, d)
            self.models.append(model)
        # print(len(self.models)) TEST
    
    #Finds a word in the model. Limit the about of corresponding sentences extracted.
    # Takes 2 parameters - String Word to find and an Int sentence Limit
    def find(self, word, sentence_limit):
        # print(self.models)
        for model in self.models:
            for words in model:
                if word == words.get_word():
                    print ("\nWORD: " + words.get_word() , "DOCUMENT: " + words.get_document() , "OCCURENCES: ", words.get_occurences())
                    print("\n")
                    sentences = words.get_sentence()
                    for i, s in enumerate(sentences):
                        if i >= sentence_limit:
                            break
                        print(s.get_index(), s.get_line())
                        print("\n")
    #OUTPUT Should be: Word: Ozzie; Document 1: 56; SENTENCES: 18 The word is ...

    # Gets the the top x words, and extracts y sentence limit
    # Takes 3 params - int word_range: that lists how many words to show. boolean show_sentence: whether to show sentences; sentence_limit: how many corresponding sentences to extract. 
    def order(self, word_range, show_sentence, sentence_limit):
        for model in self.models:
            print("===================================================" + model[0].get_document())
            for index, words in enumerate(model):
                if index > word_range:
                    break
                print ("\nWORD: " + words.get_word() , "DOCUMENT: " + words.get_document() , "OCCURENCES: ", words.get_occurences())
                if show_sentence:
                    sentences = words.get_sentence()
                    for i, s in enumerate(sentences):
                        print (s.get_index(), s.get_line())
                        print("\n")
                        if i >= sentence_limit:
                            break


            
        

