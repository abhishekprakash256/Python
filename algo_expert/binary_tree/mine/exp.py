'''
factorial program
'''

def factorial_iter(num: int) -> int:
	'''
	The function takes a number and gives back the factorial value

	Argumnets - 

		num : integer, The number for which factorial value has to be found

	------------------------------------------------------
	Return - 

		val: intger , the calculated factorial value

	'''

	#itertaive solution 

	#start the loop 

	val = 1

	for i in range(num-1):

		#calulate the fatorial 

		val = (val) * (num-i)


	return val


#print(factorial_iter(num = 3))


def factorial_rec(num: int) -> int:
	'''
	The function takes a number and gives back the factorial value

	Argumnets - 

		num : integer, The number for which factorial value has to be found

	------------------------------------------------------
	Return - 

		val: intger , the calculated factorial value

	'''

	#reursion solution

	#exit case num = 0, exit

	if num == 0 :
		val = 1

	else : 

		val =  (num) * factorial_rec(num - 1)
		


	return val

print(factorial_rec(num = 5))