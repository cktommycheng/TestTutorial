# -*- coding: utf-8 -*-
"""
Created on Wed Sep 21 13:23:49 2016

@author: Tshark
"""

def sort(lst, offset = None) :

	# set the offset to the last index of lst
	if(offset is None) :
		offset = len(lst) - 1
	
	# checking for the base case of the recursion. i.e, to stop iterating when offset has reached 0
	if(offset >= 0) :
		# recursive step
		lst = sort(lst, offset - 1)
		
		# set the value of ele to the offset, we assume this to be the smallest element
		ele = offset

		# for loop to find the smallest element in range (offset, len(lst))
		for i in range(offset + 1, len(lst)) :
			# change the smallest element index i.e. ele , if smaller element is encountered
			if(lst[ele] > lst[i]) :
				ele = i

		# swap the element at offset with that at ele
		tmp = lst[offset]
		lst[offset] = lst[ele]
		lst[ele] = tmp

		# print the lst at that point
		print("\n\nSTEP " + str(offset + 1) + " : ")
		for i in range(0, len(lst)) :
			print(lst[i])

	return lst



data = ["new york", "san fransisco", "delhi", "sydney", "london", "paris", "rome", "los angeles"]
sort(data)