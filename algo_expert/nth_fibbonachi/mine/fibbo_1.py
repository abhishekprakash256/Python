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

	#the recursive apporach 
	
	fibbo_sum = 0
	#edge case is 0 is 0 
	if num == 1: 
		return 0

	#edge case is 1 is 1 
	if num == 2:
		return 1

	#add the last two numbers
	else :
		fibbo_sum = fibbo_fun(num - 1) + fibbo_fun(num - 2)

	return fibbo_sum

print(fibbo_fun(9))