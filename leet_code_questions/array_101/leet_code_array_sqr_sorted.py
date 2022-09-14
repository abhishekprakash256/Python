"""
The square of elements in the array , the numbers are sorted 
in the output array 
"""

#test case 

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
		squared_lst = []
		for i in nums:
			squared_lst.append(i*i)

		squared_lst.sort()

		return squared_lst

if __name__ == '__main__':
	Soln = Solution()
	res = Soln.sortedSquares(Input)
	print(res)