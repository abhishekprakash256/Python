"""
the question is for the merging for the sorted array and 
create a new array of the sorted elements 
"""

#test cases

nums1 = [1,2,3] 
m = 3 
nums2 = [2,5,6] 
n = 3
Output: [1,2,2,3,5,6]




class Solution:
	def merge(self, nums1, m: int, nums2, n: int) -> None:
		"""
		Do not return anything, modify nums1 in-place instead. 
		"""	
		nums1_ptr = 0
		nums2_ptr = 0

		if m > n:
			length = m

			while nums1_ptr < length:

				if nums1[nums1_ptr] == nums2[nums1_ptr]:
					nums1.insert(nums1_ptr,nums2[nums1_ptr])
					nums1_ptr +=1
					nums2_ptr+=1

				elif nums1[nums1_ptr] <  nums2[nums1_ptr]:
					nums1_ptr +=1
				
				elif nums1[nums1_ptr] > nums2[nums1_ptr]:
					nums1.insert(nums1_ptr+1,nums2[nums1_ptr])
					nums1_ptr+=1
					nums2_ptr+=1

		else:
			length = n

			while nums2_ptr < length:
				

				



		return nums1

if __name__ == '__main__':
	Soln = Solution()
	res = Soln.merge(nums1,3,nums2,3)
	print(res)