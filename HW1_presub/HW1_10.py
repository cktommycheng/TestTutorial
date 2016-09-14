# -*- coding: utf-8 -*-
"""
Created on Tue Sep 13 20:45:17 2016

@author: Tommy Cheng
"""

#12 
def lingo():
    guesslst = []
    word = list("fuzzy")

    while guesslst != word:
        new = []
        guess = input("Enter word: ")
        guesslst = list(guess)
        for x in guesslst:
            if x in word:
                for y in word:
                    if x == y:
                        if word.index(y) == guesslst.index(x):
                            if x not in new:
                                new.append("[%s]" % x)
                        else:
                            if x not in new:
                                new.append("(%s)" % x)
            else:
                if x not in new:
                    new.append(x)
        print("".join(new))
    print("Congratulations you win! The word was %s" % "".join(word))


def main():
    print("Loading word list from file...")
    print("Welcome to the game, Lingo!")
    lingo()
    
lingo()