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
 

#print the list 

def print_list(head):
	"""
	print the linked list

	"""
	cur = head

	while cur is not None:
		print(cur.data)
		cur = cur.next

	return "List is printed"


def rescursive_print(head):
	"""
	the recursve apprach to print

	"""
	if head is not None:
		print(head.data)

		rescursive_print(head.next)

	return ("List is printed")
## a->b->c->d

print(print_list(a))

print(rescursive_print(a))


























