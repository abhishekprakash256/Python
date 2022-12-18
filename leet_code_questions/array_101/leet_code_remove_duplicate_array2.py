"""
Remove the duplicate elements from the array on the same array and modify it 

"""

nums = [1,1,2]
out = [1,2]

nums2 = [0,0,1,1,1,2,2,3,3,4,4,4]
out2 = [0,1,2,3,4]

nums3 = [1,1,1,1,2]
out3 = [1]


"""
The apprach is the two pointer approach 
one before and other a one point after that 
both the pointer are inccrease if not matches 
remove the right point and move the array
"""

class Solution:
	def removeDuplicates(self,arr):
		"""
		The function takes the array and remove the duplicates and modify array on the place 
		Args:
			arr : (list) the increasing order arranged array 
		"""

		left,right = 0,1

		if len(arr) == 0:
			return arr

		while (right < len(arr)) :
			
			if (arr[left] == arr[right]):
				arr.remove(arr[right])
			else:
				left +=1
				right +=1


if __name__ == '__main__':
	sol = Solution()
	print(nums3)
	res = sol.removeDuplicates(nums3)
	print(nums3)