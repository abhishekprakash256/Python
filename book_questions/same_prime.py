"""
The function takes two numbers and check if both of them have same prime divisor

34, 51 - 17


"""

def check_prime(number:int) ->int:
	"""
	The fuction checks for the prime number


	"""

	count = 0

	for i in range(1,number+1):

		if number % i == 0:

			count+=1

			if count>2:

				return True

	return False



def same_prime(num_1:int , num_2:int) ->int:
	"""
	The function checks two numbers has the same prime divisor or not

	Arguments:
		num_1 (int) -> the integer value

	Return:

		prime_val (int) -> the common integer value
	"""

	smaller_num = num_2

	if num_1 < num_2:
		smaller_num = num_1

	for i in range(2,smaller_num+1):

		if (num_1 % i) == 0 and (num_2 % i == 0):

			if check_prime(i) == False:

				return "Have same prime divisor"


	return "Not same prime divisor"




print(same_prime(4,51))

