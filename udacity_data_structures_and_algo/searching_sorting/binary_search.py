"""
Implement the binary search from scratch 
in a list
"""

"""
take the divide it array 
take the middle element and compare it and if can't be divided then peek the left and right 
based on that go to the left array or the right array
repeat it again till the element found 
if not found return False
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


class Searching:
	def binary_search(self,arr,target):
		"""
		The fucntion takes the value of the array and the searching val 
		and search the val in the array
		Args:
			arr : (list) The integer of the array 
			target : (int) the value of the integer to search 
		Return:
			True or False: (bool) The element found or not 
		"""

		left = 0
		right = len(arr) - 1
		mid = (left + right) // 2 

		while left <= right:

			if target == arr[mid]:
				return "Found"

			elif target < arr[mid]:
				right = mid - 1
				mid = (left + right) // 2
			else:
				left = mid + 1
				mid = (left + right) // 2 

		return "Not Found"

if __name__ == '__main__':
	sol = Searching()
	res = sol.binary_search(lst2,target2)
	print(res)