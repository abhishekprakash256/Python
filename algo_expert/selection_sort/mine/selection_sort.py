'''
Implemenet the selection sort of the array 
Gievn an array of the unosrted numbers return the sorted array
'''


lst_0 = [1,2,3,4,5,6,7,8,9]

lst_1 = [1,2,4,4,4,4,3,5,6,7,8,9]

lst_2 = [0,21,32,4,50,6,7,81,9]

lst_3 = [1,2,3,4,5,6,7,89,9]

lst_4 = [1,2,3,4,5,6,7,89,9,9,9,9,9]

lst_5 = [100,2,3,4,5,6,7,89,9,9,9,9,91]

lst_6 = [100,9,9,9,9,9]


def selection_sort(array : list) -> list:
	'''
	The funtion is used for the implementation of the selection sort

	Arguments:
		array (list) - the list of the unsorted numbers 

	Returns:
		array (list) - the list of the sorted numbers

	'''

	length_of_lst = len(array) - 1  #getting the length 

	i = 0  #start of the looping 

	while i < length_of_lst:  #the first loop

		j = i  #start from same position

		while j < length_of_lst: #the inner loop

			#swappin condition 

			if array[i] > array[j+1]:

				temp = array[i]

				array[i] = array[j+1]

				array[j+1] = temp

			j+=1

		i+=1

	return array 


print(selection_sort(lst_5))