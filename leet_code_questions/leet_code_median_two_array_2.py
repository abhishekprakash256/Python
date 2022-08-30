"""
The question is to find the median of the two sorted array

[1,2] ,[3] = [2]

[1,2] , [3,4] = [2.5]

[0] , [0] = [0]
"""

#test cases

inp1 = [1,2]
inp2 = [3,4]
out1 = 2.5

inp3 = [1,2]
inp4 = [3]
out2 = 2

inp5 = [0]
inp6 = [0]
out3 = [0]






class Solution:
	def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
		"""
		The function to find the median of the two array
		Args:
			nums1 (lst) - the list of the number
			nums2 (lst) - the list of the number
		Returns:
			median (float) - the median of the two list
		"""

		#check the length

		combined_array = nums1 + nums2 
		combined_array.sort()
		if len(combined_array) % 2 == 0:
			#do the two calculation
			point_1 = int(len(combined_array)/2) 
			point_2 = int(len(combined_array)/2 - 1)
			median = (combined_array[point_1] + combined_array[point_2])/ 2
			return median
		else:
			point_1 = int((len(combined_array) - 1)/2)
			#do the even calulation 
			median = combined_array[point_1]
			return median





if __name__ == '__main__':
	soln = Solution()
	res = soln.findMedianSortedArrays(inp5,inp6)
	print(res)
