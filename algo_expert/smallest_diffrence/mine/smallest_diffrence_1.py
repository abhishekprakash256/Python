'''
to find the smallest diffrence between the integers in given two lists

'''

#test cases 

test_01 = [-1,5,10,20,28,3] 

test_02 = [26,134,135,15,17]


#sorted list [-1,3,5,10,20,28]     , [15,17,26,134,135]


def smallest_diff(lst_1:list, lst_2: list)-> list:
	'''
	Function to compute the diffrence between the number in two integer list

	Arguments:
		lst_1 (list) -> the array of the numbers 
		lst_2 (list) -> the array of the numbers 

	Returns:
		first, second (int) -> the two numbers whose diffrence is smallest
	'''
	#sorting the list

	lst_1.sort()

	lst_2.sort()

	diff = float('inf')

	i = 0 

	j = 0 

	len_lst = len(lst_1) - 1 

	#start the loop 

	while (i or j) < len_lst :

		print(i,j)

		new_diff = lst_1[i] - lst_2[j]

		new_diff = abs(new_diff)

		if (float(new_diff)) < diff or (lst_1[i] < lst_2[j]):

			diff = new_diff

			num_1 = lst_1[i]

			num_2 = lst_2[j]

			if i < len_lst:

				i+=1

			else:

				i=i

		else:

			if j < len_lst:

				j+=1

			else:

				j=j 




print(smallest_diff(test_01, test_02))

