"""
The binary search implementation of the recursion approach

"""

#test cases


lst0 = [1,2,3,4,5,6,7]
target0 = 3  # True , not passed

lst1 = [1,2,3,4,5,6,7,8]
target1 = 5  # True , not passed

lst2 = [1,2]
target2 = 3 #True , not passed

lst3= [1]
target3 = 1  #True, not passed


lst4 = [1,2,3,4,5]
target4 = 1



def binary_search(nums:list, target:int) :
	"""
	The implemetation of the binary search in the recursion form
	Args:
		nums: (list) The list of the numbers
		target: (int) The integer of the val to find 
	Return:
		True or False: (False) The value is found or not
	"""

	length = len(nums)
	mid = length // 2

	if len(nums) >= 1:
		if nums[mid] == target :
			return "Found"
		elif nums[mid] > target :
			return binary_search(nums[0:mid],target)
		else :
			return binary_search(nums[mid+1:len(nums)],target)
	else:
		return "Not Found"

if __name__ == '__main__':
	res = binary_search(lst4,target4)
	print(res)