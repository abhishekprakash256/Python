"""
You are given an m x n integer matrix matrix with the following two properties:

    Each row is sorted in non-decreasing order.
    The first integer of each row is greater than the last integer of the previous row.

Given an integer target, return true if target is in matrix or false otherwise.

You must write a solution in O(log(m * n)) time complexity.

"""


#test cases 

mat0 = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
tar0 = 3 
out0 = True

mat1 = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
tar1 = 13 
out1 = False

mat2 = [[],[]]
tar2 = 2
out2 = True

mat3 = [[1],[1]]
tar3 = 1
out3 = True


#wrong solution


#----------------------------------------not working -------------------------------------------------
class Solution:
	def searchMatrix(self,matrix:list,target:int)->bool:
		"""
		The function take the matrix and search for the desred output and returns True or False
		Args:
			matrix: (list) The matrix of the integers
			target: (int) The number to search for 
		Return:	
			True or False: (bool) The target found or not 
		"""

		left = [0,0]
		right = [len(matrix)-1,len(matrix[0])-1]


		while left[0] <= right[0] and left[1] <= right[1]:

			mid = [(left[0] + right[0])//2, (left[1] + right[1])//2]

			if matrix[mid[0]][mid[1]]  == target:
				return True

			elif target > matrix[mid[0]][mid[1]]:
				left = [mid[0]+1,mid[1]+1]

			else:
				right = [mid[0] - 1, mid[1] - 1]

		return False

sol = Solution()
res = sol.searchMatrix(mat0,tar0)

print(res)