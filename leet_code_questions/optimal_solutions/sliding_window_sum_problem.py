'''
finding the sum of the number in the list and making the dynamic array of the lst
makingt the array of the dynamic length, and making the sum 
'''

class Sum:
	def max_sum_arr(self,arr,k):
		max_sum = float('-inf')
		start = 0
		curr_sum = 0 
		for end,val in enumerate(arr):
			curr_sum += val
			if end - start + 1 == k:
				max_sum = max(max_sum, curr_sum)
				curr_sum -= arr[start]
				start+=1
		return max_sum


lst = [1,2,3,4,5,6,7,8]
lst_2= [2,3,4,1,5]

array = Sum()
print(array.max_sum_arr(lst_2,3))


'''
def max_sum_arr(arr,k):
	max_sum = float('-inf')
	start = 0
	curr_sum = 0 
	for end,val in enumerate(arr):
		curr_sum += val
		if end - start + 1 == k:
			max_sum = max(max_sum, curr_sum)
			curr_sum -= arr[start]
			start+=1
	return max_sum


lst = [1,2,3,4,5,6,7,8]

print(max_sum_arr(lst,3))'''