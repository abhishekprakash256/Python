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
		num_even = 0
		for i in nums:
			count = 0
			while True:
				if i/10 < 1:
					count+=1
					break
				else:
					i = i/10
					count+=1
			if count % 2 ==0:
				num_even +=1

		return num_even


if __name__ == '__main__':
	Soln = Solution()
	res = Soln.findNumbers(Input2)
	print(res)