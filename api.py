import re
from wordmodel import WordModel
from sentence import SentenceModel


# Doc Scanner Find Word
# test_(mFile, mWord):
#     line_numbers = []
#     mWord = '\s' + mWord + '\s'
#     print(mWord)
#     # mWord = "\b".join(mWord).join("\b")
#     for index, lines in  enumerate(f, 0):
#         # print (index,lines) WORKS
#         hits = re.findall(mWord, lines, re.IGNORECASE)
#         if len(hits) > 0:
#             print (index, lines)
#     #         # ArrayList Add line number
#             # line_numbers.append(index)
#     # print (line_numbers)


def get_string_from_file(mFile):
    file_as_string = mFile.read()
    mFile.close()
    return file_as_string
    

# Create a Dictionary with each word. No Duplicates.
def create_dictionary(file_as_string):
    # Remove Punctuation / Capitalization
    return dict.fromkeys(re.sub('[.,]','', file_as_string).lower().split())


# Iterate through each entry in the dict; scan the document 
# using regex to get numOccurences add to Dict.
def rank_dictionary(myDict, file_as_string):
    for keys in myDict:
        pattern = '\s' + keys + '\s'
        occurences = re.findall(pattern, file_as_string, re.IGNORECASE)
        myDict[keys] = len(occurences)
    return order_dictionary(myDict)

# Order the Dictionary according to Num Occurences
def order_dictionary(myDict):
    dictList = []   
    for key, value in myDict.items():
        temp_dictionary = {}
        temp_dictionary["word"] = key
        temp_dictionary["occurence"] = value
        dictList.append(temp_dictionary)

    dictList.sort(key=lambda x: x["occurence"], reverse=True)
    # print (dictList)

    return dictList
    # [
    #   {word: the, occurence: 5}
    #   {word:  hi, occurence: 7}
    # ]

    # Build a WordModel[] list and return it
def build_model(mList, file_as_string, doc_):
    model = []
    lines = file_as_string.splitlines()
    # print(mList[0]["word"])
    # Iterate through listDic; finding the setence data
    # Create the WordModel
    # listDict[0] = {word: x, occurence: y}
    for dictItem in mList:  #For each word
        pattern = '\s' + dictItem["word"] + '\s'
        wordSentences = []
        for index, l in enumerate(lines): #For Each Line
            hits = re.findall(pattern, l, re.IGNORECASE)
            # print(len(hits))
            if len(hits) > 0:
                mSentence = SentenceModel(l, doc_, index)
                wordSentences.append(mSentence)
        wordModel = WordModel(dictItem["word"], doc_, dictItem["occurence"], wordSentences)
        model.append(wordModel)
    return model



