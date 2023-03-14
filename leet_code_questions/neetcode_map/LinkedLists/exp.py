"""

make the logic for the list popping and addition 
"""

lst = [1,2,3,4,5,6,7]

def popper(lst):
	

	
	alt = False
	head = False
	i = 0
	length = len(lst) - 1
	new_lst = []

	while i <= length:

		if head == False:
			first = lst.pop(0)
			new_lst.append(first)
			head = True

		elif alt == False:
			last = lst.pop()
			new_lst.append(last)
			alt = True

		else:
			first = lst.pop(0)
			new_lst.append(first)
			alt = False
		i+=1

	return new_lst


res = popper(lst)
print(res)	
