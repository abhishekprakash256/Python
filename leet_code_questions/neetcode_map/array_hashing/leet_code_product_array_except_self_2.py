"""
Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs inO(n)time and without using the division operation.

"""

#You must write an algorithm that runs in O(n) time and without using the division operation.


nums = [1,2,3,4]
out =[24,12,8,6]


nums2 = [-1,1,0,-3,3]
out2 = [0,0,9,0,0]


nums3 = []
out3 = []

nums4 = [0,0,0]
out4 = [0,0,0]


class Solution:
	def productExceptSelf(self, nums: list) -> list:
		"""
		The function takes the list and the calculate the multiplication of the nums in the list 
		Args:
			nums : (list) The list of the nums 
		Return:
			mul_lst : (list) The listf of the nums 
		"""
		forward_mul = []
		reverse_mul = []
		product_arr = []
		mul_forw = 1
		mul_backward = 1

		for i in nums:
			mul_forw = mul_forw *i
			forward_mul.append(mul_forw)
		
		for j in reversed(nums):
			mul_backward = mul_backward*j
			reverse_mul.insert(0,mul_backward)
			
		for k in range(len(nums)):
			if k == 0:
				product_arr.append(reverse_mul[1])
			elif k == (len(nums) - 1):
				product_arr.append(forward_mul[len(nums) - 2])
			else:
				product_arr.append(forward_mul[k-1]*reverse_mul[k+1])

		return product_arr



if __name__ == '__main__':
	sol = Solution()
	res = sol.productExceptSelf(nums2)
	print(res)


"""

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res=[1]*len(nums)
        prefix=1
        for i in range(len(nums)):
            res[i]=prefix
            prefix*=nums[i]
        postfix=1
        for i in range(len(nums)-1,-1,-1):
            res[i] *= postfix
            postfix *= nums[i]
        return res
"""