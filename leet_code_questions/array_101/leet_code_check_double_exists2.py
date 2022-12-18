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

		double_map = {}

		for i in arr:
			if float(i)/2 in double_map or i*2 in double_map:
				return True
			double_map.update({i:True})
		return False

if __name__ == '__main__':
	sol = Solution()
	res = sol.checkIfExist(arr3)
	print(res)
