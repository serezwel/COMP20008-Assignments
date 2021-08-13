## Part B Task 3
import re
import sys
import pandas as pd
import nltk
import os

def preprocess(f):
    file_text = re.sub("[^a-zA-Z\n\s\t]", " ", f.read())
    file_text = re.sub("[\n\t]", " ", file_text)
    file_text = re.sub("[\s]{2}", " ", file_text)
    file_text = re.sub("[A-Z]", lambda lower_case: lower_case.group().lower(), file_text)
    return file_text

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
        if keyword_list[i].lower() in tokenized_text:
            boolean_keyword[i] = True
    if all(boolean_keyword):
        docID_list.append(docID.loc[docID['filename'] == filename, 'documentID'].item())
print(docID_list)



