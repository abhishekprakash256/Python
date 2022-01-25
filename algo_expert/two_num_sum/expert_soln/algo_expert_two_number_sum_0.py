'''
the two sum problem, return the two numbers from the list whose sum is equal to a given number
can have negative numbers in lst
no number is repetative

'''

#make the test cases - 

lst_0 = [1,2,3,4,5,6,7,8,4,8,9] #normal case
sum_0 = 3 
out_0 = 1,2

lst_1 = [0,1,2,3,4,5,6,7,8,4,8,9] # not have sum number case
sum_1 = 100
out_1 = None

lst_2 = [0,-1,-2,3,4,5,6,7,8,4,8,9] #negative number case 
sum_2 = -3 
out_2 = 1,2

lst_3 = [0,1,2,3,4,5,6,7,8,4,8,9] #repeating sum case
sum_3 = 8 
out_3 = 0,8

lst_4 = [0,1,2,3,4,5,6,7,8,4,8,9] #normal case
sum_4 = 17
out_4 = 8,9


def sum_of_two_num_0(lst : list , sum : int)-> tuple:
	'''
	The function takes a distinct number list of numbers and a Sum number
	calulates the pair of number whose sum is equal to that given number

	Arguments:
		lst : list , distint list of the numbers

	Returns:
		pair_numbers: tuple, two number whose sum is equal to given number
	'''

	#optimize solution

	#dictionary implementation

	sum_left = {}

	#start the loop

	for i in range(len(lst)):
		#calculation of the value for the remaining sum

		remain = sum - lst[i]

		if remain in sum_left:
			return remain , lst[i]
		
		else:
			#sum_left[lst[i]] = True
			sum_left.update({lst[i]:True})


	return None
		

print(sum_of_two_num_0(lst = lst_4 , sum = sum_4)) #run time O(n) , memory O(n)
