"""
The function takes the array it is sorted and deletes the elemets that are repetative in the array
the array is modified on the place without creating copies
"""

nums = [1,1,2]
out = [1,2]

nums2 = [0,0,1,1,1,2,2,3,3,4,4]
out2 = [0,1,2,3,4]

nums3 = [1,1,1,1,2]
out3 = [1]


#the one poingter apprach but doesn't passs the 3rd case ---------------------------------------------------------------

class Solution:
	def removeDuplicates(self, nums: list) -> int:
		self.nums = nums
		"""
		The function makes the array has all the unique elememts 
		Args:
			nums : (list) The array of the unique elements 
		"""
		i = 0 
		while (i < len(self.nums) - 1) :
			#print(self.nums[i])
			if self.nums[i] == self.nums[i+1]:
				print(i)
				nums.remove(nums[i])
			i+=1
			


if __name__ == '__main__':
	soln = Solution()
	print(nums3)
	res = soln.removeDuplicates(nums3)
	print(nums3)
