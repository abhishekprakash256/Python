'''
chapter 1 , quaetion - 8
The program to swap the two numbers without using the third variable
'''


def swap(num_1:int , num_2: int)-> int:
	"""
	the function takes the two numbers and swap them
	
	Arguments: 
		num_1, num_2 (int) - the integers numbers 

	Returns:

		num_1, num_2 (int) - the swapped numbers 
	"""

	num_1 , num_2 = num_2, num_1

	return num_1, num_2


print(swap(2,3))