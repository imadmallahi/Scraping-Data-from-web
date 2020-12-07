# -*- coding: utf-8 -*-
"""
Created on Fri Oct 11 09:55:44 2019

@author: user
"""

import nltk
nltk.download('stopwords')

from nltk.corpus import stopwords

stopwords_en = stopwords.words('english')
stopwords_ar = stopwords.words('arabic')
stopwords_fr = stopwords.words('french')



print ("\n stps_en",stopwords_en)
print ("\n stps_ar",stopwords_ar)
print ("\n stps_fr",stopwords_fr)
