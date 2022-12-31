"""
The binary tree implementatio from scratch 
using the node 
"""

class Node():
	def __init__(self,data):
		self.data = data
		self.left = None
		self.right = None

class tree():
	def __init__(self):
		self.root = None

	def insert_node(self,data):
		node = Node(data)
		temp = self.root

		if self.root is None:
			self.root = node

		elif temp.data < data : 
			if temp.left is None:
				temp.left = node
			else:
				self.insert_node(data)
		
		elif temp.data > data:
			if temp.right is None:
				temp.right = node
			else:
				self.insert_node(data) 
		else:
			if temp.left is None:
				temp.left = node
			if temp.right is None:
				temp.right = node
			else:
				self.insert_node(data)


my_tree = tree()
my_tree.insert_node(4)
my_tree.insert_node(5)



print(my_tree.root.data)
print(my_tree.root.left.data)
