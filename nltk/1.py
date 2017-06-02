

import nltk

text="Mary had a little lamb. Her fleece was white as snow"
from nltk.tokenize import word_tokenize, sent_tokenize
sents=sent_tokenize(text)
print(sents)