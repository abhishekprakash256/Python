"""
The function makes the random number order in the list and shuffle the numbers 

"""

import random

def random_lst(lst: list)-> list:
	"""
	The functiion takes the list and shuffle the list

	Arguments:
		lst (list) -> the array of the numbers 

	Returns:
		shuffle_lst (list) -> the array of the numbers shuffled


	"""
	
	for i in range(len(lst)):

		random_num = random.random()

		lst[i] = lst[i]