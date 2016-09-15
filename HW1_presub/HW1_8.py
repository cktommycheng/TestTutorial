# -*- coding: utf-8 -*-
"""
Created on Sat Sep 10 01:18:47 2016

@author: Tommy Cheng
"""

'''Problem 8 : Guess the number game: this program asks user to guess a number between
0 to 20 inclusively. The user has infintely many trials. When the user guesses it correctly,
it will 


'''

import random

num = random.randint(1, 20)     #generate a number between 1 to 0 inclusively
print(num)

print('Hello! What is your name?')
name = input('Enter your name: ')
print('\n',name,',', 'I am thinking of a number between 1 and 20. Take a guess.')

guess = 0           #initiate a varible
counter = 0         #counter

while guess!= num:
    guess = input('Your guess(integer): ')
    guess = int(guess)
    if guess < num:                     #if guess is lower than the answer, prompt user to enter again
        counter = counter + 1
        print('Your guess is too low. Take a guess')
    elif guess > num:                   #if guess is higher than the answer, prompt user to enter again
        counter = counter + 1
        print('Your guess is too high. Take a guess')
    elif guess == num:                  #if guess is right, end program and print our the total number of guesses
        counter = counter + 1
        print('Good job,',name,'! You guessed my number in', counter, 'guesses !')
