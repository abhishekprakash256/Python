"""
to find the len of the list

"""

l1= [1,2,3,4,5]


def length_list(lst):
	count = 0
	for i in lst:
		count+=1
	return count


print(length_list(l1))