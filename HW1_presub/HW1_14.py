# -*- coding: utf-8 -*-
"""
Created on Sat Sep 10 05:31:32 2016

@author: Tommy Cheng
"""
'''Problem 14: Alternade: This program prints all the alternade of every word in 
the wordbank taken alternatively in a strict sequence, and used in the same order as the original word,
make up at least two other words. All letters are be used, but the
smaller words are not necessarily of the same length. It will not print if the alternade only has fewer than 2 words
'''

file = open('wordlist.txt')
wordbank = file.read().split()
wordlist1, wordlist2 = [], []

smallword_1 = ''
smallword_2 = ''


for word in wordbank:               #go throgh the each word in the wordbank
    smallword_1 = ''                #create a temporary variable to store a small word
    smallword_2 = ''                #create a temp variable to store another small word
    word_1 = ''             #temp variable, check to see if the str is empty, if so it will not print
    word_2 = ''               #same purpose as the above for 

    length = 0
    
    if len(word) == 1:             #Case1: if the word has 1 letter
        print('"' + word + '": makes no word.')
    elif(len(word)>1):              #Case2: if the word has more than 1 letter
        for i in range(len(word)):
            #print(i)
            if i%2==0:                 #extract the even position letter(letter in position, 0, 2, 4, ...)
                smallword_1 = smallword_1 + word[i]   #combine the even position letters to form a word
            elif i%2 ==1:               #extract the odd position letter(letter in position, 1, 3, 5, ...)
                smallword_2 = smallword_2 + word[i] #combine the even position letters to form a word
    for j in range (len(wordbank)):
        if(smallword_1 == wordbank[j]):     #check if smallword 1 exists in the wordbank
            word_1 = wordbank[j]
        elif smallword_2 == wordbank[j]:     #check if smallword 2 exists in the wordbank
            word_2 = wordbank[j];
    


    if word_1 != '' and word_2 !='':        #if both aren't empty, print the strings
        print(word + ' makes ' + word_1 +' and ' + word_2 +'\n')
    
                

                
        
