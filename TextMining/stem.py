# -*- coding: utf-8 -*-
"""
Created on Fri Oct 11 10:02:21 2019

@author: user
"""

import nltk 
from nltk.stem.porter import PorterStemmer
stemmer = PorterStemmer()

stem = stemmer.stem("accomplish")
print(stem)

stem = stemmer.stem("accomplished")
print(stem)

stem = stemmer.stem("accomplishing")
print(stem)