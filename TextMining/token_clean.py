# -*- coding: utf-8 -*-
"""
Created on Fri Oct 11 10:25:30 2019

@author: user
"""
##Emaple of corpus-raw text preprossing
import nltk
nltk.download('stopwords')
nltk.download('stopwords')
from nltk.corpus import stopwords
from nltk.tokenize import WordPunctTokenizer
from nltk.stem.porter import PorterStemmer
from nltk.corpus import stopwords

#RegexpTokensizer class : A RegexplTokenizer
from nltk.tokenize import RegexpTokenizer

stemmer = PorterStemmer()

raw_text="""
Preprocessing methods depend on specific application. In 
many applications, such as Opinion Mining or Natural Language Processing (NLP),
 they need to analyze the message from a syntactical point of view, which requires
 that the method retains the original sentence structure. Without this information,
 it is difficult to distinguish “Which university did 
 the president graduate from?” and “Which president is a graduate of Harvard University?”, 
 which have overlapping vocabularies. In this case, we need to avoid removing the
 syntax-containing words.
 """

#lowercase 
text= raw_text.lower()
print("\n------------raw text :\n",text)


#Tokenizee using RegexpTokee,izer

tokenizer = RegexpTokenizer(r'\w+')#remove also puntion
token  = tokenizer.tokenize(text)


print("\n-------------- Tokenzer :\n :", token )

#Stop word removal 


stopwords_en = stopwords.words('english')
tokens_clean = [t for t in token if  t not in stopwords_en]

print("\n ------------ stop word removal : tokens_clean \n",tokens_clean)


#Stemming using PorterStemmer()
stems =[stemmer.stem(t) for t in tokens_clean]
print("\n ------------ Stemming : stem  \n",stems)
