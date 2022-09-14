"""
same question not using the sortred method 
using the sorting logic implementation 

"""


#test cases 
Input = [-4,-1,0,3,10]
Output = [0,1,9,16,100]


Input2 = [-7,-3,2,3,11]
Output2 = [4,9,9,49,121]



class Solution:
	def sortedSquares(self, nums: int) -> int:
		"""
		The function makes the square of the list numbers
		and sort the array
		Args:
			nums(list) : the list of the integers 
		Returns:
			squared_list (list) : the sorted list of the squaures of the num
		"""
		sorted_lst = []

		sorted_map = {}

		for i in nums:
			#to make the storage
			



		return nums 


if __name__ == '__main__':
	soln = Solution()
	res = soln.sortedSquares(nums)
	print(res)