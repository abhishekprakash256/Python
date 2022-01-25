"""
The function to implement the merger sort algorithm in the given unsorted list

"""

test_0 = [1,23,4,65,7,87]

test_1 = [3,3,5,6,2,5,7,8,42]

test_2 = [1,1,1,12,3,4,0,0,0]




def merge_sort(lst:list)-> list:
	"""
	The function to do the merge sort of the list elements

	Arguments:
		lst (list) -> the list of unsorted array elements

	Return:

		sorted_lst (list) -> the soreted list of the array
	"""

	#calculation of the mid

	if len(lst)> 1:

		mid = len(lst)//2

		#divide the array 

		left = lst[:mid]

		right = lst[mid:]

		#pass to split ,recursion

		merge_sort(left)

		merge_sort(right)


		#start to merge

		i = 0

		j = 0 

		k = 0

		#start a loop to copy

		while i < len(left) and j < len(right):

			if left[i] < right[j]:

				lst[k] = left[i]

				i+=1

			else:

				lst[k] = right[j]

				j+=1

			k+=1


		#look for the remaing element 


		while i < len(left):

			lst[k] = left[i]

			i+=1

			k+=1

		while j < len(right):

			lst[k] = right[j]

			j+=1

			k+=1


	return lst




print(merge_sort(test_2))




