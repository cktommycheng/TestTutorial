# -*- coding: utf-8 -*-
"""
Created on Sat Sep 10 02:28:13 2016

@author: Tshark
"""
'''Problem 11: This program is a sentence splitter can split a text into
sentences. It will print every sentence in every line
'''

import re

text2 = '"Droll?" said Mr. Newman, laughing too. "Did you ever hear of Christopher Columbus?"'
text = "Mr. Smith bought cheapsite.com for 1.5 million dollars, i.e. he paid a lot for it! Did he mind? Adam Jones Jr. thinks he didn't. In any case, this isn't true... Well, with a probability of .9 it isn't."


#This is a split function 
#the first argument (?<!\w\.\w.) 
#?<! prevents the split if the following conditions satisfy:
#\w = word character [a-z, A-Z, 0-9_] followed by \. = '.' followed by 
#\w match any word character [a-z, A-Z, 0-9_]
#. matches any character (except newline)

#the second argumnt (?<![A-Z]\.)  
#?<! prevents the split if the following conditions satisfy:
#[A-Z] matchesA-Z a single character in the range between A and Z uppercase followed by
#\. matches the character.

#the third argument (?<![A-Z][a-z]\.)
#?<! prevents the split if the following conditions satisfy:
#A-Z a single character in the range between A and Z upper case followed by 
#[a-z] match a single character present in a-z a single character followed by 
#\. matches the character .

#the fourth argument (?<=\.|\?|\!)\s
#?<= allows the split if the following conditions satisfy:
#\. = '.' or \? = '?' or \! = "!" followed \s = any white space


sentence = re.split('(?<!\w\.\w.)(?<![A-Z]\.)(?<![A-Z][a-z]\.)(?<=\.|\?|\!)\s' , text)


for line in sentence :
    print(line + '\n')

#-------------------------------------------------------------------------------------------------------------------------


