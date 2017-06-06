
import nltk

text="neden  yazmak bu kadar zordur ki . Kalem yorulur mu sence "
from nltk.tokenize import word_tokenize, sent_tokenize
sents=sent_tokenize(text)
#print(sents)

words=[word_tokenize(sent) for sent in sents]
#print(words)

from nltk.corpus import stopwords 
from string import punctuation
customStopWords=set(stopwords.words('english')+list(punctuation))

wordsWOStopwords=[word for word in word_tokenize(text) if word not in customStopWords]
#print(wordsWOStopwords)

from nltk.collocations import *
bigram_measures = nltk.collocations.BigramAssocMeasures()
finder = BigramCollocationFinder.from_words(wordsWOStopwords)
#print(sorted(finder.ngram_fd.items()))
print(nltk.pos_tag(word_tokenize(text)))