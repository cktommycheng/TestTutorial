# -*- coding: utf-8 -*-
"""
Created on Wed Sep 21 13:25:45 2016

@author: Tshark
"""

co=[1,2,5,10,50,100,200]
comb=[]

def iter_fun(sum1, myString, Total):	
	if sum1>Total:
		return None	
	#print(myString)
	if sum1==Total:
		myseq=myString.split()
		myseq=[int(x) for x in myseq]
		print(myseq)
		myseq.sort()
		comb.append(myseq)
	for i in co:
		iter_fun(sum1+i,myString + str(i)+' ',Total) 

def fixed_sum_digits(Tot):
	iter_fun(0,"",Tot)
	#print(comb)
	comb.sort()
	l=len(comb)
	i=1
	while i<l:
		if comb[i-1]==comb[i]:
			comb.pop(i)
			i-=1
			l-=1
		i+=1
	
	#print(comb)
	print(str(len(comb)) + " combinations are possible")
	for i in comb:
		lc=len(co)
		n1=[0]*lc
		for j in i:
			n1[co.index(j)]+=1
		pr=''
		for i in range(lc):
			pr = pr + str('\t') + str(co[i]) + str('*') + str(n1[i]) + str(' ')
		print(pr)


				

fixed_sum_digits(200)