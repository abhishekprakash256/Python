"""
A given list of the numbers , the function takes that list and print all the integers that are even first the odd ones
Chapter 9 , question - 8
"""

test_0 = [1,2,3,4,5,6,7,8,9]

test_1 = [3,4,6,8,12,5,8,9,1,3]

test_2 = [2,2,3,4,5,67,12,5,7,9]



def even_odd(lst: list) -> list:
	"""
	The function takes the list of the integers and given the even integers first and then odd intergers 
	"""

	new_lst_0 = []

	new_lst_1 = []

	for i in lst:

		if i % 2 == 0:

			new_lst_0.append(i)

		else:

			new_lst_1.append(i)


	return new_lst_0 + new_lst_1

print(even_odd(test_0))