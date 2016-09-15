"""
Created on Thu Sep 15 06:58:12 2016

@author: TommyCheng
"""
"""
Problem 2:  This program is a semordnilap
recogniser that accepts a file name 
from the user and finds and prints all pairs of words that are
semordnilaps to the screen. 
"""


filename = input("Enter filename: ")        #prompt user for input
file = open(filename)

text = file.read().split()     #read the file and split the words into a list

semordnilap_list= []        #create a storage list

for word1 in text:          #nest for loop: 1st loop go through the wordbank
    for word2 in text:      #2nd loop goes through the wordbank again
        if word1 == word2[::-1]:    #check to see if the word is semordnilap 
            print(word1, word2)     #print words that are semordnilap
    
file.close()