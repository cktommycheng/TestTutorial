# -*- coding: utf-8 -*-
"""
Created on Thu Sep 15 14:32:55 2016

@author: Tommy Cheng
"""
'''
    Problem 6: This program prompts user to enter a text file name, it will create a new text file in
    which all the lines from the original file are numbered from 1 to n
    (where n is the number of lines in the file).
'''

filename = input("Enter filename: ")    #ask for user input in the local directory 
file = open(filename)
line = file.readline() # read first line. This ensures proceeding loop runs at least once

i = 1            # assign iterator to number lines
    
 
new_text = ''       #create an empty str variable

while line:                     #loop through the line of the original file
    new_text += str(i) + ' '    #add the line number
    new_text += line            #add the line
    i += 1                      # add 1 to iterator
    line = file.readline()      #read the next line of the file
    
file.close()                    #closes the original file


new_filename = input('Enter a new file name: ')
new_file = open(new_filename, 'w')
new_file.write(new_text)
new_file.close()
    


