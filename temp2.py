import re

def poke_names(file_name):
	# Get all the names from the file
	with open(file_name, 'r') as f:
		names = re.findall(r'\w+', f.read())

	# Prepare our lists
	longest_series, current_series = [], []

	# Returns the index of the next word that starts with the last letter
	# of the previous word
	def name_starts_with(lastletter, names):
		for index, name in enumerate(names):
			if name.startswith(lastletter):
				return index
		return False

	# This is where the magic happens
	# For each name in the pokemon names list
	for name in names:
		current_name = name
		current_series.append(current_name) # Add the first name to the series

		namelist = names[:] # Make a copy of the names list
		namelist.pop(namelist.index(current_name)) # Remove the first name from the list

		index = name_starts_with(current_name[-1], namelist) # Get the index of the next name

		# As long as there will be a name that starts with the last letter
		# of the previous word
		while index is not False:
			current_name = namelist[index] # Get this name
			current_series.append(current_name) # Add it to the series
			namelist.pop(index) # Remove it from the list
			index = name_starts_with(current_name[-1], namelist) # Get the position of the next one

		# If the current series... ah, this is pretty self explanatory
		if len(current_series) > len(longest_series):
			longest_series = current_series

		# Empty our current series for the next loop
		current_series = []

	# Print the longest series
	print(longest_series)

#test
poke_names('pokemon.txt')