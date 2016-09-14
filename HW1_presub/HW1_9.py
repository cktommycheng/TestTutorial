# -*- coding: utf-8 -*-
"""
Created on Sat Sep 10 01:38:28 2016

@author: Tommy Cheng
"""
#9
import numpy
import random

color = ['orange', 'yellow', 'blue', 'red', 'brown']
num = random.randint(0, len(color)-1)
word = color[num]


def anagramgenerator(choice):
    order = numpy.random.choice(len(choice), len(choice), replace = False)
    print(order)
    anagram = ''
    for i in range(len(order)):
        anagram = anagram + choice[order[i]]
    return(anagram)
    

anagram = anagramgenerator(word)

def anagramGame():
    stop = False
    print('***Anagram***\n')
    print('Color word anagram: ',anagram,'\n')
    while stop == False:    
        userinput = input('Guess the color word: ')
        if userinput != word:
            print('Incorrect, guess again.')
        elif userinput == word:
            stop = True
            print('Correct!')
            
anagramGame()
        