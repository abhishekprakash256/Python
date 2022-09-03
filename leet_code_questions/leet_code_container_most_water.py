"""
Find the area of the water that has most of the area, from the list of the numbers 
"""

#test cases

inp = [1,8,6,2,5,4,8,3,7]
out = 49 

inp2 = [1,1]
out2 = 1


inp3 = [1,2,4,5,6,8]
out3 = 12



class Solution:
	def maxArea(self, height: list) -> int:
		"""
		The function finds the max area from the list
		Args:
			height (lst) : The list of the integers of the bars 
		Returns:
			area (int) : The max area 
		""" 
		temp_area = 0 

		max_area = 0

		for i in range(len(height)):
			for j in range(i+1, len(height)):
				temp_area = (abs(height[i] - height[j])) * ((j - i))
				if temp_area > max_area:
					max_area = temp_area


		return max_area 

if __name__ == '__main__':
	soln = Solution()
	res = soln.maxArea(inp)
	print(res)
