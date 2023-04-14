"""
make a doubly linked list for the python
implemnmt the remove from pos
inplement the addition on the tail 
implemnt the addition on the head
"""



class Node:
	def __init__(self,val = None):
		self.val = val
		self.next = None
		self.prev = None


class Double_linked_list():
	def __init__(self):
		self.head = None
		self.tail = None


	def set_head(self,val):
		"""
		set the head
		""" 
		node = Node(val)

		if self.head is None:
			self.head = node

	def set_tail(self,val):
		"""
		set the tail
		"""
		node = Node(val)

		if self.tail is None:
			self.tail = node
			self.head.next = self.tail
			self.tail.prev = self.head

		else:
			temp = self.tail
			temp.next = node
			node.prev = temp
			self.tail = node



	def set_node(self,val):
		"""
		set the node after the head
		"""

		node = Node(val)

		temp = self.head
		temp_nxt = temp.next
		
		while True:

			if temp_nxt is self.tail:

				temp.next = node
				node.prev = temp
				node.next = temp_nxt
				temp_nxt.prev = node
				break


			temp = temp.next
			temp_nxt = temp.next

		return "set node done"


	def set_priority(self,val):
		"""
		get the priority and set the new head
		"""

		temp = self.head

		while True:

			if temp.val == val:

				#--- make the node in the middle -------
				temp_nxt = temp.next
				temp_prev = temp.prev 
				temp_prev.next = temp_nxt
				temp_nxt.prev = temp_prev

				#--------make the head -----------------
				temp.next = self.head
				self.head.prev = temp
				self.head = temp
				break

			temp = temp.next

		return "The value not found"



	def print_list(self):
		"""
		To print the list
		"""
		
		temp = self.head

		while True:

			print(temp.val)

			if temp.next is None:
				break

			temp = temp.next




if __name__ == "__main__":
	linked_lst = Double_linked_list()
	linked_lst.set_head(1)
	linked_lst.set_tail(6)
	linked_lst.set_node(2)
	linked_lst.set_node(3)
	linked_lst.set_node(4)
	linked_lst.set_node(5)
	linked_lst.set_priority(3)
	linked_lst.set_priority(5)
	linked_lst.set_priority(4)
	linked_lst.set_tail(7)
	linked_lst.set_tail(8)

	

	print(linked_lst.print_list())