"""
The function gives two numbers whose sum is equal to a target number

"""

#test cases

test_0 = [1,22,4,56,8,7,9]
target_0 = 15 #7,8

test_1 = [1,1,1,1,1,2]

target_1 = 4

lst_2 = [0,-1,-2,3,4,5,6,7,8,4,8,9] #negative number case 
sum_2 = -3 
out_2 = -1,-2

lst_3 = [0,1,2,3,4,5,6,7,8,4,8,9] #repeating sum case
sum_3 = 8 
out_3 = 0,8

lst_4 = [0,1,2,3,4,5,6,7,8,4,8,9] #normal case
sum_4 = 17
out_4 = 8,9




def sum_two_num(lst:list, target:int)-> tuple:
	"""
	The function takes the array of numbers and gives two numbers whose sum is equal to target numnber

	Arguments:
		array (list) -> the array of integers

	Returns:

		num_1 , num_2 (int) -> the numbers whose sum is equal to target

	"""

	sum_left = {}

	#start the loop

	for i in range(len(lst)):
		#calculation of the value for the remaining sum

		if (target - lst[i]) not in sum_left:

			sum_left.update({lst[i]:True})

		else: 
			return target - lst[i], lst[i]


	return None
		
print(sum_two_num(test_1, target_1))