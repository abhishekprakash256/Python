'''
find the largest three numbers in the array and return it 
return the list of three numbers, in sorted array increasing order
'''

test_0 = [2,3,5,1,1,4,6,8]  #pass
out_0 = [5,6,8]

test_1 = [1,1,1,1,1,1,1] # notpass
out_1 = [1,1,1]

test_2 = [2,5,1,1,2,2,8]  #pass
out_2 = [2,5,8]

test_3 = [5,5,5,5,1,1,1,0] #pass
out_3 = [0,1,5]

test_4 = [9,1,1,2,2] #pass
out_4 = [1,2,9]

test_5 = [1,1,1,1,1,1,1,2] # not pass
out_5 = [1,1,2]


def three_largest_num(array : list) -> list:
	'''
	the function takes the unsorted array of the integers
	gives out the list of three greatest numbers in a list

	Arguments:

		lst (list) - the array of unsorted integers

	Return:

		sub_lst (list) - the three largest number from the given array  
	'''

	sub_lst = [None, None , None]

	i = 0 

	while i < len(array):

		#pass to a helper function

		i+=1

	return sub_lst




print(three_largest_num(test_0))