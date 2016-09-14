# -*- coding: utf-8 -*-
"""
Created on Sat Sep 10 01:18:47 2016

@author: Tommy Cheng
"""

#Problem 8 

import random

num = random.randint(1, 20)
print(num)

print('Hello! What is your name?')
name = input('Enter filename: ')
print('\n',name,',', 'I am thinking of a number between 1 and 20. Take a guess.')

guess = 0 
counter = 0

while guess!= num:
    guess = input('Your guess(integer): ')
    guess = int(guess)
    if guess < num:
        counter = counter + 1
        print('Your guess is too low. Take a guess')
    elif guess > num: 
        counter = counter + 1
        print('Your guess is too high. Take a guess')
    elif guess == num:
        counter = counter + 1
        print('Good job,',name,'! You guessed my number in', counter, 'guesses !')
