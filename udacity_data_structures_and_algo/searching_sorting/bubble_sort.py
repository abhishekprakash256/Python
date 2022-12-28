"""
The implemantion of the bubble sort 
replace the value as compare to the next and replace till sorted
"""

lst = [1,2,4,5,1,45,7,8]
	#  0,1,2,3,4,5,6

lst1 = [1,1,1,1,1,2,2,2,2]

lst2 = [2,2,2.3,3,3,0]


class Sorting:
	def bubble_sort(self,nums:list):
		"""
		The implementaion of the bubble sort for the list
		Args:
			nums : (list) The list of the numbers
		Return:
			nums : (list) The sorted list of the numbers
		"""

		for i in range(len(nums) ):

			for j in range(len(nums) - 1):

				if nums[j] > nums[j+1]:
					nums[j],nums[j+1] = nums[j+1],nums[j]

		return nums

if __name__ == '__main__':
	sol = Sorting()
	res = sol.bubble_sort(lst)
	print(res)