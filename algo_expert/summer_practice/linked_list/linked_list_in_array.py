"""
The program to make the link list in the array 

"""

"""
create a linked list from scratch in python

"""
class Node():
	"""
	Made a node in the list 
	"""
	def __init__(self,data):
		self.data = data
		self.next = None

#class Linked_list():




a = Node(1)
b = Node(2)
c = Node(3)
d = Node(4)

a.next = b
b.next = c
c.next = d


def linked_lst_array(head):
	"""
	The fucntion takes the head of the list and convert the 
	whole list to the array

	"""
	linked_lst = []
	current = head
	while current is not None:
		linked_lst.append(current.data)
		current = current.next

	return linked_lst


new_lst = []


def linked_lst_array_rec(head,lst):
	"""
	The print of the list in the recursive solution

	"""
	if head is not None:
		new_lst.append(head.data)

		linked_lst_array_rec(head.next,new_lst)

	return new_lst


print(linked_lst_array(a))
print(linked_lst_array_rec(a,new_lst))