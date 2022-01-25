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


def three_largest_num(lst = list)-> list:

	'''
	The function takes the lst and returns the three largest integers 

	Arguments :
		lst (list) - The list of the intergers
	-------------------------------------------

	Returns :
		sub_lst (list) - the largest three numbers from the given list

	'''


	#make the sublst 

	sub_lst = []

	#sort the array 

	lst.sort()  #using the sort function from the python 

	#start variable

	i = 0 

	#look the last three elemets traverse backward

	lst.reverse()  #also using the reverse

	#set the counter 

	count = 0

	#loop over the elements

	lst.append(None)

	while i < len(lst)- 1 and count < 3:

	#if element change append other wise keep traversing

		if lst[i] != lst[i+1]:
			
			sub_lst.append(lst[i])
			
			count+=1

		i+=1

	#cheap trick to make length three

	if len(sub_lst) == 1 :

		sub_lst.append(sub_lst[0])
		sub_lst.append(sub_lst[0])

		sub_lst.reverse()

		return sub_lst
	
	elif len(sub_lst) == 2:

		sub_lst.append(sub_lst[1])

		sub_lst.reverse()

		return sub_lst

	else:

		sub_lst.reverse()

		return sub_lst


print(three_largest_num(test_0))