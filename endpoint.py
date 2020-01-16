import api
import wordmodel
from documentscanner import DocumentScanner

# 1) Document Scanner
# Document Scanner is a reusable module that can scan or order words in a txt document. It may be used as either an API endpoint, 
# external library, or strapped on to a view in Django.

# 2) MVVM
# Document Scanner works with an MVVM architecture in mind;  WordModel and SentenceModel are View Models.
# Using Django we can attach a view layer. 
# DocumentScanner produces a Model that can be queried multiple times. This is evident in running both find and order sequentially where the time and o(n) improves significantly. 


# 3) Problems and Bugs
# APOSTROPHE: 
# Well Noted problem with ' character. This seperates plurals from non plurals for example children's. The problem was that we could not strip
#  ' as non posessives such as i'm or they've would not work. The solution given more time would be to create a list of non posessive apostrophe words
#  and ommit the list from the search.
# 
#  0/NON DETECTION: 
#  Some words are showing 0 sentences and 0 word occurences. Not sure why this is the case but presume it may be with the fact that the struct holding the premodel changes from a
# dict to a list holding a dict; then eventually to an object. 


#4) Example 
documents = ["doc1.txt", "doc2.txt", "doc3.txt", "doc4.txt", "doc5.txt", "doc6.txt"]
mDocScanner = DocumentScanner(documents)

# find(word:"string", sentence_limit:int) - finds a word from all documents and show corresponding information
# word - word to find; 
# sentence_limit: how many sentences with the word you want to fetch
mDocScanner.find("long", 5)
# mDocScanner.find("America", 3)
# mDocScanner.find("capital", 3)

# order(num_most_frequent_words:int, include_sentences:boolean, num_sentences_to_fetch:int ) - orders a list of the x most frequent words with y included sentences. 
mDocScanner.order(7,False, 3)

# Gets the Models to be queried in a custom way. Returns a list of WordsModel objects that contain data.
# mDocScanner.getModels()

# 5) Consideration and Evaluation
# The biggest consideration in regards to something I would rewrite have everything in the view model from the first instance. Instead I query the file_string 3 times. 
# Once to get each word unique. Second to get the occurences for ordering. Finally extracting the sentences. It may be more productive to query the list once getting all the relevant
# Data then re ordering everything. Thus also avoiding changing structures 3 times.