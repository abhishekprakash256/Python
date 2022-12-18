"""
check the array if the double of the array exists or not
in the given array of the integers 
"""

arr = [10,2,5,3]

arr2 = [3,1,7,11]


class Solution:
	def CheckIfExists(self,arr):
		"""
		The given function checks whether the given array has the double or not 
		Args:
			arr : (list) The list of the ingtegers 
		Returns:
			True or False : (Bool) on the value that exists or not
		"""
		double_hash = {}

		for i in arr:
			double_val = 2*i
			if double_val not in double_hash:
				double_hash.update({i:True})
			else:
				return True
				
		return False


if __name__ == '__main__':
	sol = Solution()
	res = sol.CheckIfExists(arr2)
	print(res)