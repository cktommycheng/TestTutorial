# -*- coding: utf-8 -*-
"""
Created on Sat Sep 10 01:38:28 2016

@author: Tommy Cheng
"""
'''
Problem 9 : This program is anagram game. It will generate an anagram from a random word in t
given list and prompt user to guess the word.
'''
import numpy
import random

color = ['orange', 'yellow', 'blue', 'red', 'brown', 'purple', 'green']        #word list
num = random.randint(0, len(color)-1)                       #generate a random color 
word = color[num]


def anagramgenerator(choice):
    order = numpy.random.choice(len(choice), len(choice), replace = False) #this line generates order of position of the letter of anagram, replacement of letter is not allowed)
    anagram = ''
    for i in range(len(order)):                 #this combines the letter to anagram according to the position
        anagram = anagram + choice[order[i]]
    return(anagram)
    

anagram = anagramgenerator(word)

def anagramGame():                          #execution of the game
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
        