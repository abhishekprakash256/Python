'''
do the insertion sort in the array of the given values

'''


lst_0 = [1,2,3,4,5,6,7,8,9]

lst_1 = [1,2,4,4,4,4,3,5,6,7,8,9]

lst_2 = [0,21,32,4,50,6,7,81,9]

lst_3 = [1,2,3,4,5,6,7,89,9]

lst_4 = [1,2,3,4,5,6,7,89,9,9,9,9,9]

lst_5 = [100,2,3,4,5,6,7,89,9,9,9,9,91]

lst_6 = [100,9,9,9,9,9]

def insertion_sort(array:list)-> list:
	'''
	the function takes the list of the unsorted array and gives the sorted array

	Arguments:
		array (list) - the array of the unsorted integers

	Returns:
		array (list) - the array of the sorted integers  
	'''

	#get the length of the array 

	length_of_lst = len(array) -1

	
	#start of the loop itre

	i = 0 

	while i < length_of_lst:

		j= i

		#the outer loop of the list

		while j!= -1:

			#the inner loop of the list

			#the conditon of the the traversing and the swapping

			if array[j+1] < array[j]:

				temp = array[j]

				array[j] = array[j+1]

				array[j+1] = temp

			j-=1


		i+=1


	return array




print(insertion_sort(lst_6))

