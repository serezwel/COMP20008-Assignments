# Part B Task 2
import re
import os
import sys


input_argument = sys.argv[1]

new_dir = re.search("[^0-9]*", input_argument)
os.chdir("./" + new_dir.group())
filename = re.search("[0-9]{3}.txt", input_argument)
f = open(filename.group(), "r")
def preprocess(f):
    file_text = re.sub("[^a-zA-Z\n\s\t]", " ", f.read())
    file_text = re.sub("[\n\t]", " ", file_text)
    file_text = re.sub("[\s]{2,}", " ", file_text)
    file_text = re.sub("[A-Z]", lambda lower_case: lower_case.group().lower(), file_text)
    return file_text

print(preprocess(f))

