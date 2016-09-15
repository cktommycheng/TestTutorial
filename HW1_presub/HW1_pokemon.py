# -*- coding: utf-8 -*-
"""
Created on Sat Sep 10 02:53:21 2016

@author: TommyCheng
"""
'''
This program generates the/a sequence with the highest possible
number of Pokemon names where the subsequent name starts with
the final letter of the preceding name from a givenlist. No Pokemon name is to be
repeated. 

'''



pokeList = ["audino","bagon","baltoy","banette","bidoof", "braviary", "bronzor", "carracosta","charmeleon","cresselia", "croagunk", 
"darmanitan", "deino", "emboar", "emolga", "exeggcute", "gabite", "girafarig", "gulpin", "haxorus", "heatmor", "heatran", "ivysaur", "jellicent", "jumpluff", "kangaskhan","kricketune", "landorus", "ledyba", "loudred", "lumineon", "lunatone", "machamp", "magnezone", "mamoswine","nosepass", "petilil", "pidgeotto", "pikachu", "pinsir", "poliwrath", "poochyena", "porygon2",
"porygonz", "registeel", "relicanth", "remoraid", "rufflet", "sableye", "scolipede", "scrafty", "seaking",
"sealeo", "silcoon", "simisear", "snivy", "snorlax", "spoink", "starly", "tirtouga", "trapinch", "treecko","tyrogue", "vigoroth", "vulpix", "wailord", "wartortle","whismur","wingull" ,"yamask"]

finalList = []  # this is the final list


def solve(newList):
	global finalList,pokeList

	flag = 0
	for name in pokeList:		
		if((len(newList) == 0) or (name not in newList and (name[0] == newList[-1][-1]))):
			# this condition checks if list is empty or first letter of name mathces last letter of last element of list
			flag = 1
			newList.append(name)
			# append the name and recurs
			solve(newList)
			# pops the element for backtracking and hence also looks at other possiblities
			newList.pop()
	

	if(flag == 0):
		# flag is 0 if non of the element matches the condition, hence our sequence is complete
		# check for size of current sequence with the final list

		if (len(newList) > len(finalList)):
			finalList = list(newList)

def main():
	solve([])

	print(len(finalList))
	print("The elements are :")
	for name in finalList:
		print(name)


main();




        
        
    
       

    
    