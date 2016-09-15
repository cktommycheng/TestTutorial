# -*- coding: utf-8 -*-
"""
Created on Thu Sep 15 06:58:47 2016

@author: TommyCheng
"""
'''
Problem 5: This function return all its hapaxes. Hapaxes are words which
occur only once in either the written record of a language, the
works of an author, or in a single text. 
'''


import string

filename = input("Enter filename: ")
file = open(filename)
text = file.read().lower()

for pun in string.punctuation:          #get rid of punctuation by replacing it to "")
    text= text.replace(pun,"")
word_list = text.split()                #split the text into words only 
    
hapax = set()                   
repeat = set()          #count for duplicates

for word in word_list:
    if word not in hapax:           #add words if it is not in hapax
        hapax.add(word)
    else:
        repeat.add(word)        #add the repeated word in this list
    if word in repeat:          #remove the repeated words from hapaxes
        hapax.remove(word)
        
print('The hapaxes are: ')
for w in hapax:
    print(w)





