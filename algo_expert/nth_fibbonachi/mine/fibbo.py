'''
The question is to print the nth fibbonachi numbers as given input

numbers are - 0,1,1,2,3,5,8,13,21,34

			  1,2,3,4,5,6,7,8,9,10
'''

def fibbo_fun(num: int )-> int:
	'''
	the function will return the fibbonachi numbers as per given input

	Arguments:
		num: interger , the number till give fibbonachi number
	------------------------------------------------------------
		return : integer, the number at num position in fibbonachi series 
	'''

	#num is zero

	#num is 1 

	#start the loop 

	sum_fibbo = 0
	lst = []

	for i in range(num):

		#grab the egde case for zero
		if i == 0:
			sum_fibbo = 0
			lst.append(sum_fibbo)

		#grab the edge case for 1 
		elif i == 1:
			sum_fibbo = 1
			lst.append(sum_fibbo)

		#add the last two numbers to get final number
		else: 
			lst.append(lst[i-2] + lst[i-1])

	return lst[i]


print(fibbo_fun(1))