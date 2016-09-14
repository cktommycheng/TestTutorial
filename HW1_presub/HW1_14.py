# -*- coding: utf-8 -*-
"""
Created on Sat Sep 10 05:31:32 2016

@author: Tommy Cheng
"""
#Alternade

file = open('wordlist.txt')
wordbank = file.read().split()
wordlist1, wordlist2 = [], []

smallword_1 = ''
smallword_2 = ''


for word in wordbank:
    smallword_1 = ''
    smallword_2 = ''
    word_1 = ''
    word_2 = ''

    length = 0
    
    if len(word) == 1:
        print('"' + word + '": makes no word.')
    elif(len(word)>1):
        for i in range(len(word)):
            #print(i)
            if i%2==0:
                smallword_1 = smallword_1 + word[i]
                #print(smallword_1)
            elif i%2 ==1:
                smallword_2 = smallword_2 + word[i]
    for j in range (len(wordbank)):
        if(smallword_1 == wordbank[j]):
            word_1 = wordbank[j]
        elif smallword_2 == wordbank[j]:
            word_2 = wordbank[j];
    
#    print(word_1)
#    print(word_2)
    
    if word_1 != '' and word_2 !='':  
        print(word + ' makes ' + word_1 +' and ' + word_2 +'\n')
    
#        wordlist1.append(smallword_1)
#        wordlist2.append(smallword_2)
#    smallword_1 = ''
#    smallword_2 = ''
    
#   print(wordlist1)
#    print(wordlist2)
                

                
        
