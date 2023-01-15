"""
Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

You must write an algorithm that runs in O(n) time.
"""

#test cases

nums = [100,4,200,1,3,2]
out =  4 

nums2 = [0,3,7,2,5,8,4,6,0,1]
out2 = 9

nums3 = []
out3 = []

nums4 = [1,1,1,1]
out4 = 1 

nums5 = [-1,-2,-3,-4,6,7]
out5 = 4

nums6 = [1,2,3,4,8,9,10,11,12,13,16]
out6 = 4 

nums7 =[1,2,0,1]



#---------------------------------------------------

def max_sequence(nums:list)->int:
	"""
	The function take the list and returns the max sequence from the list
	Args:
		nums: (list) The list of the intergers unsorted
	Return:
		count: (int) The max count of the sequence that appear
	"""

	nums_set = set(nums)
	temp_count = 0

	for i in nums:
		pass
			




	return nums


if __name__ == '__main__':
	res = max_sequence(nums5)
	print(res)