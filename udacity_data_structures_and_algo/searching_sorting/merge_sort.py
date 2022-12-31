"""
The merge sort is implemented using the iterative approach 
"""

#the merge sort divide algorithm 
lst = [1,3,5,6,3,2,5,7,9,2]



def divide_lst(nums:list)->list:
	"""
	The sorting algorithm of the divide
	Args:
		nums: (list) The list of the integers
	Return:
		list: (list) The list of the divided integers
	"""
	length = len(nums)

	mid = length // 2 
	print(nums)

	if length <=1:
		return nums
	else:
		
		divide_lst(nums[0:mid])
		divide_lst(nums[mid:length])

lst2 = [1,1,2,3]

lst3 = [3,4,5,6,6]

lst4 = [1,1]
lst5 = [2,2,3]


def join_lst(nums1:list, nums2:list) ->list:
	"""
	The algorithm to join the list in the sorted manner 
	Args:
		nums1: (list) The list of the integers
		nums2: (list) The list of the interges
	Return:
		combined_lst: (list) the combined sorted list 
	"""
	if len(nums1) < len(nums2):
		temp = nums1
		nums1 = nums2
		nums2 = temp

	combined_lst = []
	i,j,k = 0,0,0
	length = len(nums1) + len(nums2) - 1
	print(length)

	while k < length:
		if i == len(nums1):
			combined_lst.append(nums2[j])
			j+=1
		
		elif j == len(nums2) :
			combined_lst.append(nums1[i])
			i+=1

		else:
			print("inside else")
			if nums1[i] == nums2[j]:
				combined_lst.append(nums1[i])
				combined_lst.append(nums2[j])
				i+=1
				j+=1
			elif nums1[i] < nums2[j]:
				print("one")
				combined_lst.append(nums1[i])
				i+=1
			elif nums1[i] > nums2[j]:
				print("two")
				combined_lst.append(nums2[j])
				j+=1

		k+=1

	return combined_lst 


def merge_sort(nums:list):
	"""
	Function take the list and sort the array using the merge sort algorithm
	Args:
		nums: (list) The list of the numbers
	Return:
		nums: (list) The list of the sorted numbers
	"""
	pass


#print(divide_lst(lst))
	
print(join_lst(lst4,lst5))