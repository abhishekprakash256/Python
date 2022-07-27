"""
make the singly linked list of the in the python
from the scrath implementation 
"""

class node():
	def __init__(self,val= None,next = None):
		self.val = val
		self.next = next


class linked_list():
	"""
	The linked list class to make the list 
	with using the nodes 
	"""
	def __init__(self):
		self.head = None

	def insert_element(self,val):
		new_node = node(val)
		if self.head == None:
			self.head = new_node
		
		else:
			curr = self.head 
			while True:
				if curr.next is None:
					curr.next = new_node
					break
				curr = curr.next

		return "the value is inserted"

	def delete_element(self,val):
		new_node = node(val)
		
		curr = self.head
		while True:
			if curr.next is new_node.val:
				curr.next = curr.next.next
				curr.next.next = None
				return "The elememt is deleted"
				break
			elif curr.next is None:
				return "The elememt is not found"
				break
			curr = curr.next

	def print_list(self):
		curr = self.head
		while True:
			if curr.next is None:
				print(curr.val)
				break
			print(curr.val)
			curr = curr.next

		return "the list is printed"





my_list = linked_list()
my_list.insert_element(4)
my_list.insert_element(5)
my_list.insert_element(6)
my_list.insert_element(7)
my_list.insert_element(8)
my_list.insert_element(9)
my_list.insert_element(10)



my_list.delete_element(7)

print(" -------------------- the list values  are being printed --------------- ")

print(my_list.print_list())


