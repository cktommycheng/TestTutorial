# -*- coding: utf-8 -*-
"""
Created on Tue Sep 13 17:16:44 2016

@author: TommyCheng
"""

#13 Bracket

import random



def generate_string(n):
    string = ''
    for i in range(2*n):
        if random.randint(0,1) == 0:
            string += '['
        else:
            string += ']'
    return(string)

def check(string):
    counter = 0;
    for i in range (len(string)):
        if string[i] == '[':
            counter += 1
        else:
            counter -= 1
            if counter <0:
                break
            
    if counter == 0:
        print(string +'\nOK')
    else:
        print(string + '\nNotOK')



check( generate_string(1))
check( generate_string(2))
check( generate_string(3))
check( generate_string(4))
