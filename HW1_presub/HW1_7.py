"""
Created on Thu Sep  8 19:23:11 2016

@author: Tommy Cheng
"""

'''Problem7
Write a program that will calculate the average word length of a text
stored in a file (i.e the sum of all the lengths of the word
the text, divided by the number of word ). 
'''


filename = input("Enter filename: ")
file = open(filename)

line = file.read()

text = line
text = text.lower() 
wordcount = 0           #set up the counter


for i in range(len(text)):
        if (ord(text[i]) > 96 and ord(text[i])<123 ):
            wordcount = wordcount +1     

#for i in range(len(text)):
#    if text[i] != ' ':
#        wordcount = wordcount + 1            

            
print(wordcount)

words = float( len(text.split()) * 1.0)

print ('The average word length of this text is: ', "%.1f"%(wordcount/words),'words' )