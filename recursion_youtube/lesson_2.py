"""
sum of natural number
"""

def sum_number(nums:int):
	"""
	The function to find the sum of the natural number
	Args:
		nums: (int) The number to find the sum 
	Return :
		sum : (int) the sum of the integers
	"""
	if nums <= 1:
		return 1
	else:
		return nums + sum_number(nums-1)

print(sum_number(4))