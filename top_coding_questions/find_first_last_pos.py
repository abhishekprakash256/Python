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


#working solution

def find_pos(nums:int, arr:list)->list:
	"""
	The function finds the position of the nums in the list of the first and the last
	and return the position in the list
	Args:
		nums: (int) The target value to find in the list
	Return:
		pos_list: (list) The first and the last index of the value in the list
	"""
	mapper = {}
	pos_lst = []

	if len(arr) == 0:
		return [-1,-1]

	for i in range(len(arr)-1):
		if arr[i] not in mapper and arr[i] == nums:
			mapper[arr[i]] = i
			pos_lst.append(i)
		mapper[arr[i]] = i

	if nums not in mapper.keys():
		return [-1,-1]
	pos_lst.append(mapper[nums])
	return pos_lst





if __name__ == '__main__':
	res = find_pos(target2,inp2)
	print(res)