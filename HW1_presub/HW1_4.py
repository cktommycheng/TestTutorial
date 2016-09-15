# -*- coding: utf-8 -*-
"""
Created on Thu Sep 15 12:54:36 2016

@author: Tshark
"""
'''
Problem 4 :This is a program speak_ICAO()able to translate any text (i.e. any string)
into spoken ICAO words with given pause time of words and letters
'''

import time
import os


#icao library
icao = {'a':'alfa', 'b':'bravo', 'c':'charlie', 'd':'delta', 'e':'echo', 
     'f':'foxtrot', 'g':'golf', 'h':'hotel', 'i':'india', 'j':'juliett', 
     'k':'kilo', 'l':'lima', 'm':'mike', 'n':'november', 'o':'oscar', 
     'p':'papa', 'q':'quebec', 'r':'romeo', 's':'sierra', 't':'tango', 
     'u':'uniform', 'v':'victor', 'w':'whiskey', 'x':'x-ray', 'y':'yankee', 
     'z':'zulu'}

def speak_ICAO(text, pauseletter, pauseword):
    words = text.lower()
    words = words.split()     #make text lowercase and split the text into individual words)
    for word in words:
              
        for letter in word:      #nest for loop to check for the letters in 
            if letter in icao:          
                os.system("say " + icao[letter])
                time.sleep(pauseletter)
        time.sleep(pauseword)


speak_ICAO("Sup bro",2,1)
