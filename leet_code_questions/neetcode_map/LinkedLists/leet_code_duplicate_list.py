"""
Given an array of integers nums containing n + 1 integers where each integer is in the range [1, n] inclusive.

There is only one repeated number in nums, return this repeated number.

You must solve the problem without modifying the array nums and uses only constant extra space.
"""


#test cases 
nums = [1,3,4,2,2]
out = 2

nums2 = [3,1,3,4,2]
out2 = 3

nums3 = [18,13,14,17,9,19,7,17,4,6,17,5,11,10,2,15,8,12,16,17]
out3 = 18

class Solution:
	def findDuplicate(self, nums: list) -> int:
		"""
		find the duplicate in the list and return the number
		"""

		mapper = {}

		for i in nums:

			if i in mapper:
				return i

			mapper[i] = True

		return False

	def findDuplicatepointer(self,nums:list)->int:
		"""
		using the two pointer 
		"""
		slow = 0
		fast = 0
		length = len(nums) - 1

		if len(nums) == 1:
			return nums[0]

		while True:



			if slow > length:  
				slow = 0

			if fast > length:

				if (fast - length) == 1:
					fast = 0 
				else:
					fast = 1

			if nums[slow] == nums[fast] and slow != fast :
				return nums[fast]

			slow+=1
			fast+=2 

			#pointer manipulation 




sol = Solution()
res = sol.findDuplicate(nums)
res2 = sol.findDuplicatepointer(nums3)

#print(res)
print(res2)