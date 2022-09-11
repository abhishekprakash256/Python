"""
to count the number of list that has the even number  of the digits
"""


#test cases 

Input = [12,345,2,6,7896]
Output = 2

Input2 = [555,901,482,1771]
output2 = 1


class Solution:
	def findNumbers(self, nums: int) -> int:
		"""
		the function to find the number of even number in the array
		Args :
			nums (int) : the number of the interger 
		Returns:
			num_even (int) : the number of the even number in the list
		"""
		
		while nums :
			


if __name__ == '__main__':
	Soln = Solution()
	res = Soln.findNumbers(Input)
	print(res)