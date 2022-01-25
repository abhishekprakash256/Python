'''
to find the smallest diffrence between the integers in given two lists

'''

#test cases 

test_01 = [-1,5,10,20,28,3] 

test_02 = [26,134,135,15,17]

test_11 = [-1,3,5,10,20,28]

test_12 = [15,17,26,134,135]



def smallest_diff(lst_1 : list , lst_2: list) -> int:
	'''
	The function takes two lists and gives two number which have smallest diffrence

	Arguments:

		lst_1 (list) -> array of integers

		lst_2 (list) -> array of integers

	Return:
		
		num_1, num_2 (int) -> two integers which have the least diffrence

	'''

	diff = float('inf')  #setting the first value

	for i in range(len(lst_1)): #start the first loop 

		for j in range(len(lst_2)):  #start the second loop

			new_diff = lst_1[i] - lst_2[j]  # checking the diffrence 

			new_diff = abs(new_diff)

			if float(new_diff) < diff: #conditional checking 

				diff = new_diff #assignments 

				num_1 = lst_1[i]

				num_2 = lst_2[j]


	return num_1 , num_2





print(smallest_diff(test_01, test_02))