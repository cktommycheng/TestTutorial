# -*- coding: utf-8 -*-
"""
Created on Thu Sep 22 17:10:53 2016

@author: Tshark
"""

'''Quesiton 7'''   
def sort(list):
    '''
    the function, sort(list), accepts a list of strings and uses recursion to 
    return a sorted list. Each step should at most modify two elements of the list.
    parameters:
    list- a list of strings
    
    return
    a list of sorted strings
    '''
    tem=list[0] #initialize a temporary string which represents biggest string 
    for i in range(1,len(list)):
        if list[i]>tem:
            tem=list[i]# read the strings one by one and give the biggest one to tem
        else:
            continue
    list.remove(tem)# remove the biggest one from list
    if list==[]:
        return [tem]# recursion end condition: if only one string left, return this one-string list
    else:
        return sort(list)+[tem]# new list will be re-sorted from small to big according to the ASCII code

sort(['you','are','good','person'])
