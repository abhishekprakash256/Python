"""
write a function that can give all the possible sub sets of the lst of numbers where all number are unique

"""

test_0 = [1,2,3,4,5,6]

test_1 = [1,2,3,45,67,8]


def sub_sets(lst:list)->int:
	"""
	The function takes the integers list and gives all the uinques sub sets

	Arguments:
		lst (list) -> the array of unique integers

	Returns:
		sub_sets (int) -> all the subsets
	"""


	print(" ,") 

	for i in range(len(lst)+1):

		print(i)

		for j in range(1,i+1):

			print(j,end =" ")

		print("")



print(sub_sets(test_0))

