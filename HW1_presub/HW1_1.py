# -*- coding: utf-8 -*-
"""
Created on Thu Sep  8 19:23:11 2016

@author: Tommy Cheng
"""
#Problem1



filename = input("Enter filename: ")
file = open(filename)


def is_palindrome(text):
    revtext = text[::-1]
    if revtext == text:
        return True

line = file.readline()
while line:
    templine = ''
    lowcaseline = line; 
    lowcaseline = lowcaseline.lower()
    for i in range(len(lowcaseline)):
        if ord(lowcaseline[i]) > 96 and ord(lowcaseline[i])<123:
            templine = templine + lowcaseline[i]
        
    if is_palindrome(templine) == True:
        print(line + 'is a palindrome.')    
    else:
        print(line + 'is not a palindrome.')
        
    templine=''
    templine2=''
        
    line = file.readline()

    
#    if templine == templine2:
#        print('Yes')
#    else:
#        print('No')

file.close()
    

    