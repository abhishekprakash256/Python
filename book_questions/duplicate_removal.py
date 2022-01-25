"""
The function removes the duplicate elements form the list , sorted list 
chapter 3 ,Question - 6

"""

#test cases

test_0 = [1,2,3,4,5,5,5,6,7]

test_1 = [0,0,0,0,1,1,2,3]

test_2 = [1,2,3,5,6,6]

test_3 = [1,2,3,6,6,7,7,8]




def remove_dup(lst: list)->list :
	"""
	The function take the sorted list and remove the sotred array

	Arguments:
		lst (list) -> the sorted array of the integers

	Returns:

		new_lst (list) -> the array with no duplicate elements
	"""

	left = 0 

	len_of_lst = len(lst) - 1

	new_lst = []

	while left < len_of_lst:

		if lst[left] != lst[left+1]:

			new_lst.append(lst[left])


		left+=1



	new_lst.append(lst[left])

	return new_lst



print(remove_dup(test_3))
