"""
The container with most of the water 

optumized solution
"""

#test cases

import time

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

		right = len(height) - 1
		left = 0

		while left < right:
			temp_area = min(height[right], height[left]) * (right - left) 

			if height[left] > height[right]:
				right -=1
			else:
				left +=1

			if temp_area > max_area:
				max_area = temp_area

		return max_area 



if __name__ == '__main__':
	soln = Solution()
	res = soln.maxArea(inp)
	print(res)
