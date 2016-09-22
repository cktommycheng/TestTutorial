# -*- coding: utf-8 -*-
"""
Created on Thu Sep 22 10:39:57 2016

@author: Tshark
"""


# S is the array of denominations that are available
# m : number of denominations
# n : amount that needs to be calculated
# ans is the string that holds the combination of denomination

def count(S, m, n , ans) :
  
  	# base case of the recursion
	if (n == 0) :
		# uncomment the below line to print all the combinations also
		# print(ans)
		return 1
	# 
	if (n < 0) :
		return 0
 

	if (m <=0 and n >= 1) :
		return 0

	temp = ''
	if(ans == '') :
		temp = ''
	else :
		temp = ans + "+"

	temp += str(S[m-1])

	# recursion step
	return count( S, m - 1, n ,ans) + count( S, m, n-S[m-1],temp)

 


arr = [1, 2, 5, 10, 20, 50, 100, 200]
m = len(arr)

print("TOTAL WAYS :: " + str(count(arr, m, 200, "")));