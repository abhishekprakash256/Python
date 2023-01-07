"""
A target value is given and the an array of the value is given , find the index when the value first appear and the last appear in the array 
return [-1,-1] if the value is not in the array or return [first_pos, last_pos]
"""

#test cases 
inp = [1,2,3,4,5,5,5,5,6]
target = 5
out = [4,7]

inp1 = [1,4,6,23]
target1 = 5
out1 = [-1.-1] 

inp2 = []
target2 = 4
out2 = [-1,-1]


inp3 = [1,2,2]
target3 = 2
out3 = [1,2]

inp4 = [6]
target4 = 6
out4 = [0]

#the solution using the binary search



#the binary search solution doesn't work for the index out of bound 

def find_elelemnt_pos(nums:int,arr:list)->list:
	"""
	The function finds the position of the target element in the sorted array
	and return the position
	Args:
		nums: (int) The target value to find in the array 
	Return:
		pos_lst: (list) The list of the target integer in the array
	"""

	if len(arr) == 0:
		return None

	pos_list = []
	arr.insert(0,"x")
	arr.append("x")
	first_pos = first_pos_finder(nums,arr)
	end_pos = last_pos_finder(nums,arr)

	pos_list.append(first_pos)
	pos_list.append(end_pos)

	return pos_list


def first_pos_finder(nums,arr):
	"""
	The binary search to find the target element in the array 
	Args:
		nums: (int) The traget integer to find in the array
		arr: (list) The array of the sorted intergers
	Return:
		first_pos: (int) The first position of the nums in array
	"""

	left = 0 
	right = len(arr) - 1

	while left <= right:
		mid = (left + right)//2

		if arr[mid] == nums and arr[mid - 1] < nums or arr[mid] == nums and arr[mid - 1] == "x":
			return mid - 1
		elif arr[mid] < nums:
			left = mid + 1
		else:
			right = mid - 1 
	return -1



def last_pos_finder(nums,arr):
	"""
	The binary search to find the target element in the array 
	Args:
		nums: (int) The traget integer to find in the array
		arr: (list) The array of the sorted intergers
	Return:
		first_pos: (int) The first position of the nums in array
	"""

	left = 0 
	right = len(arr) - 1

	while left <= right:
		mid = (left + right)//2
		
		if arr[mid] == nums and arr[mid+1] > nums or arr[mid] == nums and arr[mid + 1] == "x":
			return mid - 1
		elif arr[mid] > nums:
			right = mid - 1
		else:
			left = mid + 1
	return -1


if __name__ == '__main__':
	res = find_elelemnt_pos(target3,inp3)
	print(res)