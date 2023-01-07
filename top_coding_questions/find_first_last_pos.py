"""
A target value is given and the an array of the value is given , find the index when the value first appear and the last appear in the array 
return [-1,-1] if the value is not in the array or return [first_pos, last_pos]
"""

#test cases 


def find_pos(nums:int, arr:list)->list:
	"""
	The function finds the position of the nums in the list of the first and the last
	and return the position in the list
	Args:
		nums: (int) The target value to find in the list
	Return:
		pos_list: (list) The first and the last index of the value in the list
	"""
	