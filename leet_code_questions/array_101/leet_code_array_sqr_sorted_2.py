"""
same question not using the sortred method 
using the two pointer approach

"""


#test cases 
Input = [-4,-1,0,3,10]
Output = [0,1,9,16,100]


Input2 = [-7,-3,2,3,11]
Output2 = [4,9,9,49,121]



class Solution:
	def sortedSquares(self, nums: int) -> int:
		"""
		The function makes the square of the list numbers
		and sort the array
		Args:
			nums(list) : the list of the integers 
		Returns:
			squared_list (list) : the sorted list of the squaures of the num
		"""
		left = 0

		right = len(nums) -1 

		sorted_lst = []

		while left <= right:

			left_sqre = nums[left]*nums[left]
			right_sqre = nums[right]*nums[right]

			if right_sqre > left_sqre:
				sorted_lst.insert(0,right_sqre)
				right -=1
			else:
				sorted_lst.insert(0,left_sqre)
				left +=1
			
		return sorted_lst 

if __name__ == '__main__':
	soln = Solution()
	res = soln.sortedSquares(Input)
	print(res)