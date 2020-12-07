# -*- coding: utf-8 -*-
"""
Created on Fri Oct 11 10:15:54 2019

@author: user
"""

import nltk 
nltk.download('wordnet')
from nltk.tokenize import word_tokenize
from nltk.stem.wordnet import WordNetLemmatizer
 
def wordlemmatization():
     wordlemma =WordNetLemmatizer()
     print(wordlemma.lemmatize('cars'))
     print(wordlemma.lemmatize('walking',pos='v'))
     print(wordlemma.lemmatize('meeting',pos='n'))
     print(wordlemma.lemmatize('metting',pos='v'))
     print(wordlemma.lemmatize('better',pos='a'))
     print(wordlemma.lemmatize('is',pos='v'))
     print(wordlemma.lemmatize('funier',pos='a'))
     print(wordlemma.lemmatize('aim',pos='a'))
     
print("\n------------Word Tokenization-----------------\n")
print(wordlemmatization())
     
     