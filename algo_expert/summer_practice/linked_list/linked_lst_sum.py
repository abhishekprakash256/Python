"""
make a program to calcualate the sum of the list

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


def calc_sum(head):
	"""
	The program to find the sum of the linked list

	"""
	sum = 0
	
