# -*- coding: utf-8 -*-
"""
Created on Thu Sep 22 10:23:08 2016

@author: Tshark
"""
'''
Question 8: This program prompts user for an input of an integer and determines
whether it is a prime number 

'''

def fun1(x,n):
    """
    the function calculates the value of f(x)=3.95*（x-x**2）with n times recursion
    parameters:
    x: a number in [0,1] 
    n: numbers of recursion 
    """
    
    if n==1:        #if n=1, return base case
        return 3.95*(x-x**2) 
    else:
        return fun1(fun1(x,1),n-1) # if n!= 1, then take the value from previous iteration into the next iteration

def fun2(x,n):
    """
    the function calculuates the value function f(x)=3.95*x*(1-x）through n times recursion
    
    parameters:
    x: a number in [0,1] 
    n: number of recursion 
    """
    if n==1:     #if n=1, return base case
        return 3.95*x*(1-x) 
    else:
        return fun2(fun2(x,1),n-1) # if n!= 1, then take the value from previous iteration into the next iteration


def fun3(x,n):
    """
    the function calculates the value of f(x)=3.95*x-3.95*(x**2) through n times recursion
    
    parameters:
    x: a number in [0,1] 
    n: number of recursion 
    """
    if n==1:
        return 3.95*x-3.95*(x**2) #the end of recursion，also is the first time to cacalute the result
    else:
        return fun3(fun3(x,1),n-1) # if n!= 1, then take the value from previous iteration into the next iteration


#Test Case: n=1, n = 10, n = 50, n = 100
print("When x = 0.5 , n = 1")
print("the answers return: ", fun1(0.5, 1), fun2(0.5, 1), fun3(0.5,1) )
print("When x = 0.5 , n = 2")
print("the answers return: ", fun1(0.5, 2), fun2(0.5, 2), fun3(0.5,2) )
print("When x = 0.5 , n = 10")
print("the answers return: ", fun1(0.5, 10), fun2(0.5, 10), fun3(0.5,10) )
print("When x = 0.5 , n = 50")
print("the answers return: ", fun1(0.5, 50), fun2(0.5, 50), fun3(0.5,50) )
print("When x = 0.5 , n = 100")
print("the answers return: ", fun1(0.5, 100), fun2(0.5, 100), fun3(0.5,100))
print("When x = 0.9 , n = 100")
print("the answers return: ", fun1(0.9, 100), fun2(0.9, 100), fun3(0.9,100))


"""
Comments on the result:
As we can see, wehn the iterations go up, the answers produced by the 3 functions are
different. This is because there is a boundary on storing decimal places. As the iterations go up.
the decimals are rounded off. So each iteration contains round off error. AS the iterations go up to 
100, the round off errors accumluate, which produce different values from the 3 functions 
"""