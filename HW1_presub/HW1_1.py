# -*- coding: utf-8 -*-
"""
Created on Thu Sep  8 19:23:11 2016

@author: Tommy Cheng
"""

'''Problem 1: This function is a palindrome recogniser that accepts a file
name from the user, reads each line, and prints the line to the
screen if it is a palindrome.
'''


filename = input("Enter filename: ")    #ask for user input
file = open(filename)

#This defines a function to check to see if a word is palindrome, return true if it is"
def is_palindrome(text):
    revtext = text[::-1]
    if revtext == text:
        return True

line = file.readline()          #read line
while line:
    templine = ''               #create storage variable
    lowcaseline = line;             
    lowcaseline = lowcaseline.lower()       #convert to lower case letter
    for i in range(len(lowcaseline)):   
        if ord(lowcaseline[i]) > 96 and ord(lowcaseline[i])<123:    #use ASCII code to check for lower case alphabets in the line
            templine = templine + lowcaseline[i]
        
    if is_palindrome(templine) == True:         #if it is true, print the line and indicators
        print(line + 'is a palindrome.')    
    else:
        print(line + 'is not a palindrome.')
        
    templine=''
    templine2=''
        
    line = file.readline()


file.close()
    

    