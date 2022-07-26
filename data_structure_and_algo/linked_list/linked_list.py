"""
make the singly linked list of the in the python
from the scrath implementation 
"""

class linked_list():
	"""
	The linked list class to make the list 
	with using the nodes 
	"""
	def __init__(self,value,next =None):
		self.value = value
		self.next = next

	def itertator(self,node):
		self.node = node
		cur = self.node
		while True:
			if cur.next is None:
				print(cur.value)
				break
			print(cur.value)
			cur = cur.next





#make a simple linked list 


#making the connection in the two 




node1 = linked_list(5)
node2 = linked_list(6)
node3 = linked_list(7)
node4 = linked_list(8)

node1.next = node2
node2.next = node3
node3.next = node4


