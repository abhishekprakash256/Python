"""
Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

You must write an algorithm that runs in O(n) time.
"""

#test cases

nums = [100,4,200,1,3,2]
out =  4 

nums2 = [0,3,7,2,5,8,4,6,0,1]
out2 = 9

nums3 = []
out3 = []

nums4 = [1,1,1,1]
out4 = 1 

nums5 = [-1,-2,-3,-4,6,7]
out5 = 4

nums6 = [1,2,3,4,8,9,10,11,12,13,16]
out6 = 4 

nums7 =[1,2,0,1]


#-------------------------the solution is not in o(n) time -----------------------------------------------------

class Solution:
	def longestConsecutive(self, nums:list) -> int:
		"""
		The program to find the lomgest consecutive runs of the integers
		Args:
			nums: (list) The number list of the integers 
		Return:
			max_consecutive : (int) The consecutive array of the integers
		"""
		if len(nums) == 1:
			return 1
		elif len(nums) == 0:
			return 0

		nums.sort()
		count = 1
		max_count = 1

		for i in range(len(nums)-1):

			if nums[i]+1 == nums[i+1]:
				count +=1
			
			else:
				count = 1

			if count >= max_count:
				max_count = count

		return max_count


if __name__ == '__main__':
	sol = Solution()
	res = sol.longestConsecutive(nums7)
	print(res)