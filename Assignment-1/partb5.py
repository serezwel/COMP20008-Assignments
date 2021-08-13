## Part B Task 5
import re
import os
import sys
import pandas as pd
import nltk
import math
from nltk.stem import PorterStemmer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

ROUND_OFF = 4

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
for i in range(len(keyword_list)):
    keyword_list[i] = ps.stem(keyword_list[i])
filename_list = []
output_dict = {'documentID':[], 'score':[]}
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
        filename_list.append(filename)
        docID_list.append(docID.loc[docID['filename'] == filename, 'documentID'].item())

text_list = []
for filename in filename_list:
    f = open(filename, "r")
    text = preprocess(f)
    tokenized_text = nltk.word_tokenize(text)
    for i in range(len(tokenized_text)):
        tokenized_text[i] = ps.stem(tokenized_text[i])
    text_list.append(' '.join(tokenized_text))
vectorizer = TfidfVectorizer()

try:
    tfidf = vectorizer.fit_transform(text_list)
    vector_query = vectorizer.transform([' '.join(keyword_list)])
except ValueError:
    empty_df = pd.DataFrame.from_dict(output_dict)
    print(empty_df)
else:
    cos_sim = cosine_similarity(tfidf, vector_query)
    for i in range(len(docID_list)):
        output_dict['documentID'].append(docID_list[i])
        output_dict['score'].append(round(cos_sim[i][0],ROUND_OFF))
    df = pd.DataFrame.from_dict(output_dict)
    df = df.sort_values(by='score', ascending=False)
    df = df.set_index("documentID")
    print(df)











