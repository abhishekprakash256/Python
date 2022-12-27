"""
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

"""

#test cases 

nums = [2,7,11,15]
target = 9
Output = [0,1]


class Solution:
	def twoSum(self, nums: list, target: int) -> list:
		"""
		The program to check the sum exists as the target sum or not
		Args:
			nums : (list) The integer list of the numbers
			target : (int) The target to match the two num sum 
		Return:
			target_elements : (list) The target elements sums equal to given target
		"""

		diff_map = {}

		for i in range(len(nums)):
			if (target - nums[i]) in diff_map:
				return [diff_map[(target - nums[i])], i]
			diff_map[nums[i]] = i
		
		return False

if __name__ == '__main__':
 	sol = Solution()
 	res = sol.twoSum(nums,target)
 	print(res) 