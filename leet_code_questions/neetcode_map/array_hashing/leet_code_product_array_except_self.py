"""
Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the division operation.

"""

#You must write an algorithm that runs in O(n) time and without using the division operation.


nums = [1,2,3,4]
out =[24,12,8,6]


nums2 = [-1,1,0,-3,3]
out2 = [0,0,9,0,0]


nums3 = []
out3 = []

nums4 = [0,0,0]
out4 = [0,0,0]


#the brute force solution using the two loops runttime O(n^2)  

class Solution:
	def productExceptSelf(self, nums: list) -> list:
		"""
		The function takes the list and the calculate the multiplication of the nums in the list 
		Args:
			nums : (list) The list of the nums 
		Return:
			mul_lst : (list) The listf of the nums 
		"""
		mul_lst = []
		
		for i in range(len(nums)):
			mul = 1
			for j in range(len(nums)):
				if i == j :
					mul = 1*mul
				else:
					mul = nums[j]*mul
			mul_lst.append(mul)

		return mul_lst
if __name__ == '__main__':
	sol = Solution()
	res = sol.productExceptSelf(nums2)
	print(res)
