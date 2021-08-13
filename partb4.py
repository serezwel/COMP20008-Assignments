## Part B Task 4
import re
import pandas as pd
import os
import sys
import nltk
from nltk.stem import PorterStemmer

def preprocess(f):
    file_text = re.sub("[^a-zA-Z\n\s\t]", " ", f.read())
    file_text = re.sub("[\n\t]", " ", file_text)
    file_text = re.sub("[\s]{2}", " ", file_text)
    file_text = re.sub("[A-Z]", lambda lower_case: lower_case.group().lower(), file_text)
    return file_text

ps = PorterStemmer()
docID = pd.read_csv("partb1.csv")

os.chdir("./cricket")
keyword_list = sys.argv[1:]
docID_list = []
for filename in os.listdir():
    f = open(filename, "r")
    text = preprocess(f)
    boolean_keyword = [False] * len(keyword_list)
    for i in range(len(keyword_list)):
        tokenized_text = nltk.word_tokenize(text)
        for word in tokenized_text:
            if ps.stem(keyword_list[i].lower()) == ps.stem(word):
                boolean_keyword[i] = True
                break
    if all(boolean_keyword):
        docID_list.append(docID.loc[docID['filename'] == filename, 'documentID'].item())
print(docID_list)