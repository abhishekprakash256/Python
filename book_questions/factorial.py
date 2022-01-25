"""
The function print the factorial of the number


5 = 4*3*2*1
0 ! = 1
"""

def factorial(num:int)-> int:
	"""
	The function prints the factorial value of the number

	Argument:
		num (int) -> the integers value of the num

	Return:
		factorial_val (int) -> the factorial value


	"""


	if num == 0 or num == 1:
		return 1
	else:
		return (num)*factorial(num - 1)


print(factorial(5))