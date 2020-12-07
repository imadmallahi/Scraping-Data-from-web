# -*- coding: utf-8 -*-
"""
Created on Thu Oct 17 21:38:50 2019

@author: imad el mallahi
"""

import requests
from bs4 import BeautifulSoup
import re
import csv

import nltk
from nltk.corpus import stopwords
from nltk.tokenize import WordPunctTokenizer
from nltk.stem.porter import PorterStemmer
from nltk.corpus import stopwords

#RegexpTokensizer class : A RegexplTokenizer
from nltk.tokenize import RegexpTokenizer



def getLinks(link):
    page = requests.get(link)
    soup = BeautifulSoup(page.content, 'html.parser')
    head = soup.find('div',id="container")
    lien=head.find_all('a',href=True)
    tab=[]
    for i in lien:
        result = re.split(r"\.", i['href'])
        if 'html' in result:
            tab.append(i['href']) 
    return tab

liste=[]

def readComments(tab):
    
    for i in range(len(tab)):
        result = re.split(r"\:",tab[i])
        
        if 'https' in result:
            page = requests.get(tab[i])
        else:
            page = requests.get("https://www.hespress.com/"+tab[i])
            
        soup = BeautifulSoup(page.content, 'html.parser')
        try:
            comments = soup.find('div', id="comment_list")
            listComment=comments.find_all('div',class_="comment_body")

                
            for i in range(len(listComment)):
                 liste.append({'date': listComment[i].find('span',class_="comment_date").text.strip() , 'user':listComment[i].find('strong').text.strip(),'commit':listComment[i].find('div',class_="comment_text").text.strip()})             
                
        except:
            continue
        
        print(liste)

        
        
if __name__=='__main__':
    tab=[]
    tab=getLinks('https://www.hespress.com')
    tab=list(set(tab))
    readComments(tab)  
    en_tetes = ['date','user', 'commit']
    #create in file csv
    with open('asl_alphabet_train.csv','w',encoding='utf-8-sig') as ff:
        f_csv = csv.DictWriter(ff, en_tetes)
        f_csv.writerows(liste)
    stemmer = PorterStemmer()

    stopwords_ar = stopwords.words('arabic')
    for row in liste:
        print('date :'+row['date'])
        print('user :'+row['user'])
        print('commit :'+row['commit'])
        #lowercase 
        text= row['commit'].lower()
        print("\n------------raw text :\n",text)
        #Tokenizee using RegexpTokee,izer
        tokenizer = RegexpTokenizer(r'\w+')#remove also puntion
        token  = tokenizer.tokenize(text)
        print("\n-------------- Tokenzer :\n :", token )
        #Stop word removal     
        tokens_clean = [t for t in token if  t not in stopwords_ar]
        print("\n ------------ stop word removal : tokens_clean \n",tokens_clean)
        #Stemming using PorterStemmer()
        stems =[stemmer.stem(t) for t in tokens_clean]
        print("\n ------------ Stemming : stem  \n",stems)
        print("=======================================")
        