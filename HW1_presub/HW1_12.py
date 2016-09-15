# -*- coding: utf-8 -*-
"""
Created on Thu Sep 15 09:52:29 2016

@author: Tshark
"""

#12 Anagram

    
def two_same(string):
   for i in range(len(string)-1):
      if string[i] == string[i+1]:
         return True
   return False

def all_combo(elements):
    if len(elements) <=1:
        return elements
    else:
        temp = []
        for perm in all_combo(elements[1:]):
            for i in range(len(elements)):
                temp.append(perm[:i] + elements[0:1] + perm[i:])
        return temp
        
testlist = ['kok', 'great', 'reatg', 'tommy', 'ommty', 'greta']

filename = input("Enter filename: ")
file = open(filename)
word_list = file.read().split()

templist = []
wholelist = []


for i in word_list:
    templist = []
    sort = sorted(i)
    for word in word_list:
        counter = 0
        for letter in sort:
            if letter in word:
                counter = counter + 1
                if len(word) == counter:
                    templist.append(word)
                    wholelist.append(templist)

print(wholelist)
finlist = []

#for word in testlist:
#    if two_same(word) == False:
#        combo = all_combo(word)
#    for word2 in combo:
#        for i in range(len(testlist)):
#            if word2 == testlist[i]:
#                templist.append(word2)
#                wholelist.append(templist)
                
max = 0

for i in range(len(wholelist)):
    if (len(wholelist[i])) > max:
        max = len(wholelist[i])
for j in range(len(wholelist)-1):
    if(len(wholelist[i])) == max:
        finlist.append(wholelist[i])    
    
print(finlist)


        


    


    




