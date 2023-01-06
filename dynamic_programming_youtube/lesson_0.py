"""
first lesson for the dynamic programming
"""

#the recurcsive fibbonachi implementation 

def fib(nums:int):
	"""
	The fibbonachi implementation of the series using the recursion
	Args:
		nums: (int) The value to calculate 
	Return:
		val: (int) The value of the fibbonachi number
	"""
	if nums <=2:
		return 1
	else:
		return fib(nums-1)+fib(nums-2)




def fibb_memo(nums:int, mapper= {}):
	"""
	The fibbonachin function using the dictionary 
	Args:
		nums: (int) The value to calculate
	Return:
		val: (int) the final value of the fibbonachi series
	"""
	if nums in mapper:
		return mapper[nums]
	elif nums <= 2:
		return 1
	mapper[nums] = fibb_memo(nums-1 ,mapper) + fibb_memo(nums-2, mapper)
	return mapper[nums]

if __name__ == '__main__':
	res0 = fib(35)
	res1 = fibb_memo(35)
	print(res0)
	print(res1)