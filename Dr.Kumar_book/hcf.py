"""
the function to calculate the HCF of two numbers

2 , 6

"""

def calc_hcf(num_1:int, num_2:int)-> int:
	"""
	function to calculate the HCF of the two numbers

	Arguments:
		num_1, num_2 (int) -> the numbers to find the hcf for 

	Return:

		hcf (int) -> the hcf of the two numbers
	"""

	if num_1 > num_2:
		greater_num = num_1
	else:
		greater_num = num_2

	#to check of the hcf 

	for i in range(1,greater_num+1):
		
		if greater_num % i == 0 and num_2 % i == 0:

			hcf = i


	return hcf 



print(calc_hcf(800,500))