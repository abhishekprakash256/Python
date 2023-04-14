"""

make the logic for the list popping and addition 
"""
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
"""

mapper = {}


mapper[1] = True
mapper[2] = True
mapper[3] = True


print(mapper)

mapper.pop(2)

print(mapper)


"""
for LRU cache we need a addion methond on the back 

The most recently used value will come on the top 

and the addition value will come on the back of the dictionary 

so if we get the item it should be move to the top of the list 

if we use a list and a dict the dict has the value position for this list 

so the list can be removed and updated based on the dict value 

the most active elements are placed on the head or the left as if they are accessed 

"""

lst = []

lst = [1,3,4,5,4,6,7,8]


lst.insert(0,2)

print(lst)

lst.remove(6)

print(lst)

lst.append(9)

print(lst)


"""
make a list and the dict together with refrence as lru
"""

values = []

val_mapper = {}

values.append(1)

