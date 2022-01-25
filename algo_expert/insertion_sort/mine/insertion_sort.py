'''
implement the insertion sort with a given unsorted array 
'''


lst_0 = [1,2,3,4,5,6,7,8,9]

lst_1 = [1,2,4,4,4,4,3,5,6,7,8,9]

lst_2 = [0,21,32,4,50,6,7,81,9]

lst_3 = [1,2,3,4,5,6,7,89,9]

lst_4 = [1,2,3,4,5,6,7,89,9,9,9,9,9]



def insertion_sort(array: list) -> list:
	'''
	The function takes a unsorted array and gives back the sorted array

	Arguments:
		array (list) - The list of the unsorted numbers 

	Returns :

		array (list) - The list of the sorted numbers
	'''

	length_of_lst = len(array) - 1

	#start the loop

	i=0

	j = i

	while i < length_of_lst:

		#second loop

		j = i

		while j != 0:

			#swapping condition

			if array[j+1] < array[j]:

				print(array[j])

				#just make a temp variable

				temp = array[j]

				array[j+1] = array[j]

				array[j+1] = temp

			j -= 1

		i+=1


	return array  

print(insertion_sort(lst_1))






