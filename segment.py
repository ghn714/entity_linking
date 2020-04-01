import nltk
from nltk.corpus import stopwords
import re

def inputfile(textname):

    text = textname
    with open(text, 'r', encoding='utf-8') as file:
        u = file.read()
    str = re.sub('[^\w ]', '', u)
    tokens = str.split()
    clean_tokens = set()
    sr = stopwords.words('english')
    for token in tokens:
        if token not in sr:
            clean_tokens.add(token)
    # print(clean_tokens)
    return list(clean_tokens)
