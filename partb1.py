## Part B Task 1

import re
import pandas as pd
import os
import sys

output_filename = sys.argv[1]

os.chdir("./cricket")

valuedict = {"filename":[], "documentID":[]}
for filename in os.listdir():
    f = open(filename, "r")
    documentID = re.search("[A-Z]{4}-[0-9]{3}([A-Z]{2}|[A-Z][a-z]|[A-Z]\Z|[A-Z].|\Z|.)", f.read(), re.DOTALL)
    matched_with_article = re.match("[A-Z]{4}-[0-9]{3}([A-Z][a-z])" , documentID.group(), re.DOTALL)
    matched_with_EOF = re.match("[A-Z]{4}-[0-9]{3}([A-Z]\Z|\Z)" , documentID.group(), re.DOTALL)
    documentIDfinal = documentID.group()
    if matched_with_article:
        documentIDfinal = documentIDfinal[:len(documentIDfinal)-2]
        valuedict["filename"].append(filename)
        valuedict["documentID"].append(documentIDfinal)
    elif matched_with_EOF:
        valuedict["filename"].append(filename)
        valuedict["documentID"].append(documentIDfinal)
    else:
        documentIDfinal = documentIDfinal[:len(documentIDfinal)-1]
        valuedict["filename"].append(filename)
        valuedict["documentID"].append(documentIDfinal)
output_df = pd.DataFrame.from_dict(valuedict)
output_df = output_df.set_index("filename")

os.chdir("../")

output_df.to_csv(output_filename)
    
    

