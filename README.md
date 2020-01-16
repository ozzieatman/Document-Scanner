# Document-Scanner
AI/NLP/ML Document Scanner. Finds Word Quantities and Sorts Them

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
