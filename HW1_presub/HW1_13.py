# -*- coding: utf-8 -*-
"""
Created on Tue Sep 13 17:16:44 2016

@author: TommyCheng
"""

'''Problem 13: This program generates a string with
N opening brackets ("[") and N closing brackets ("]"), in some
arbitrary order. And it prints whether there exists complete pairs of brackets
'''

import random

def generate_string(n):
    string = ''
    for i in range(2*n):                #Here I use a random number generator to generate 
        if random.randint(0,1) == 0:    #open and close brackets
            string += '['
        else:
            string += ']'
    return(string)

def check(string):
    counter = 0;
    for i in range (len(string)):       
        if string[i] == '[':            #Here is a special way of counting, if it starts 
            counter += 1                #with a open bracket, the next bracket can either be open of close, for both cases 
        else:                           # the counter will be greater than zero. After all iterations, if the counter is zero, that means 
            counter -= 1                  #each open brackets closes properly given that the first bracket is open.
            if counter <0:              #if the counter is zero after the first iteration, it must be imcomplete because it starts with a close bracket
                break
            
    if counter == 0:            #If counter = 0, everything checks out
        print(string +'\nOK')
    else:   
        print(string + '\nNotOK')



check( generate_string(1))
check( generate_string(2))
check( generate_string(3))
check( generate_string(4))
