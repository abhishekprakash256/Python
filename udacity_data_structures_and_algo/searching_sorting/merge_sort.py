"""
The merge sort is implemented using the iterative approach 
"""

#the merge sort divide algorithm 
lst = [1,3,5,6,3,2,5,7,9,2]



def divide_lst(nums:list)->list:
	"""
	The sorting algorithm of the divide
	Args:
		nums: (list) The list of the integers
	Return:
		list: (list) The list of the divided integers
	"""
	length = len(nums)

	mid = length // 2 
	print(nums)

	if length <=1:
		return nums
	else:
		
		divide_lst(nums[0:mid])
		divide_lst(nums[mid:length])



 





def merge_sort(nums:list):
	"""
	Function take the list and sort the array using the merge sort algorithm
	Args:
		nums: (list) The list of the numbers
	Return:
		nums: (list) The list of the sorted numbers
	"""
	pass


print(divide_lst(lst))
	