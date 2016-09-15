# -*- coding: utf-8 -*-
"""
Created on Thu Sep 15 13:40:14 2016

@author: Tshark
"""
"""
Problem 3: character frequency table
   Prompt ussers for a file name. And list the frequency of all the characters
"""
import string

def char_freq_table(name):

   file = open(filename)
   text = file.read()   #read file
   
   for i in range(len(string.printable)):       # For loop: Use str.count function to count the frequency
       print(string.printable[i],' ', text.count(string.printable[i]))  # of character 


filename = input("Enter filename: ")    #ask for user input

char_freq_table(filename)