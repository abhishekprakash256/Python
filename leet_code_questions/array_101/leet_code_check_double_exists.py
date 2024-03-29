"""
check the array if the double of the array exists or not
in the given array of the integers 
"""

arr = [10,2,5,3]

arr2 = [3,1,7,11]

arr3 = [7,1,14,11]

class Solution:
	def checkIfExist(self,arr):
		"""
		The given function checks whether the given array has the double or not 
		Args:
			arr : (list) The list of the ingtegers 
		Returns:
			True or False : (Bool) on the value that exists or not
		"""
		s = set()
		for num in arr:
			if float(num) / 2 in s or num * 2 in s:
				return True
			s.add(num)
		return False


if __name__ == '__main__':
	sol = Solution()
	res = sol.checkIfExist(arr3)
	print(res)