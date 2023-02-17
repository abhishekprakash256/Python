"""
Suppose an array of length n sorted in ascending order is rotated between 1 and n times. For example, the array nums = [0,1,2,4,5,6,7] might become:

    [4,5,6,7,0,1,2] if it was rotated 4 times.
    [0,1,2,4,5,6,7] if it was rotated 7 times.

Notice that rotating an array [a[0], a[1], a[2], ..., a[n-1]] 1 time results in the array [a[n-1], a[0], a[1], a[2], ..., a[n-2]].

Given the sorted rotated array nums of unique elements, return the minimum element of this array.

You must write an algorithm that runs in O(log n) time.

"""

#test cases 

arr1 = [1,2,3,4,5]
out1 = 1


arr2 = [2,3,4,5,0,1]
out2 = 0

arr3 = []
out3 = None


arr4 = [5,6,7,0,-1,-2,-3]
out4 = -3 



class Solution:
	def findMin(self, nums: list) -> int:
		"""
		The function finds the minimum value in the array that is rotated
		Args:
			nums: The list of the numbers 
		Returns:
			min_val : The min value in the array
		"""

		res = nums[0]
		left = 0
		right = len(nums) - 1
		mid = (left + right) // 2
		
		if len(nums) == 0:
			return -1 

		if nums[left] <= nums[mid] <= nums[right]:
			return nums[0]

		while left <= right:

			#exit condn
			if nums[left] > nums[right] and (left + 1) == right:
				return nums[right]

			#find the mid	
			mid = (left + right) // 2

			#find the min
			min_val = min(nums[left], nums[mid], nums[right])

			#condn
			if min_val == nums[left] or min_val == nums[mid]:
				right = mid
			else:
				left = mid 



if __name__ == "__main__":
	sol = Solution()
	res = sol.findMin(arr1)
	print(res)