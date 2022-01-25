'''
finding the sum of the continous element that are equal to a sum given
update the size of the array as well
'''

class Solution:
	def sum_fun(self,arr,s):
		min_size = float('inf')
		start = 0
		curr_sum = 0
		for end,val in enumerate(arr):
			curr_sum += val
			while curr_sum >= s:
				min_size = min(min_size, end - start + 1)
				curr_sum -= arr[start]
				start +=1
		return min_size

lst_1 = [1,2,4,5,7,2,5,2]

soln = Solution()

print(soln.sum_fun(lst_1,14))


