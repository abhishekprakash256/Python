'''
implement the bubble sort in the list 

'''

'''suddo code 

1.set the pointer till the last of the array
2.Enurate with the two points and swap 
3.Till the last pointer is set to the second value
'''


lst_0 = [1,2,3,4,5,6,7,8,9] #sorted array 

lst_1 = [2,1,3,4,5,4,7,6,8,9] #array 

lst_2 = [1,1,1,1,2,3,5,4,4,4,4,7,8] #array 

lst_3 = [0,1,2,13,4,65,6,79,8] #array


#make the sorted function 

def buble_sort(array: list)-> list:
	'''
	The function takes a list and gives the sorted list

	Arguments:
		
		array (list) - The list of the numbers 

	Returns:

		lst (list) - The list of sorted array
	'''

	#make the last pointer 

	last_pointer = len(array) - 1

	#the start value of the pointer 

	

	#start the loop and compare 

	#the two loop approach 

	j = 0

	while j < last_pointer:

		#compare and swap the values 

		#set the inner iteration
		
		i =0

		while i < last_pointer :

			if array[i] > array[i+1]:

				temp = array[i]

				array[i] = array[i+1]

				array[i+1] = temp

			i +=1 #increase the pointer 

		j +=1

		last_pointer -=1 #decrease the last pointer 

	return array


print(buble_sort(array = lst_3))

lst_2.sort()

print(lst_2)