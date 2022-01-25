"""
1
2 1 
3 2 1
4 3 2 1 
5 4 3 2 1 

Chapter 1, question - 12
"""

def print_pattern():
	"""
	print a pattern

	"""


	for i in range(1,7):

		for j in reversed(range(1,i)):

			print(j, end=" ")

		print("")

	return " "



print(print_pattern())

			