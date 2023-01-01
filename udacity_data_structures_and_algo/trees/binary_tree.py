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
		
		else:
			while True:
				if temp.data < data:
					if temp.right is None:
						temp.right = node
						break
					else:
						temp = temp.right
				elif temp.data > data:
					if temp.left is None:
						temp.left = node
						break
					else:
						temp = temp.left
				else:
					if temp.left is None:
						temp.left = node
						break
					elif temp.right is None:
						temp.right = node
						break
					else:
						temp = temp.left

	def search_node(self,data):
		temp = self.root

		while True:
			if temp.data == data or (temp.right is None and temp.left is None):
				if temp.data == data:
					return "Found"
					break
				elif temp.right is None:
					return "Not Found"
					break
				else:
					return "Not Found"
					break
			elif temp.data < data:
				temp = temp.right
			else:
				temp = temp.left


					







#add the tree nodes 
my_tree = tree()
my_tree.insert_node(4)
my_tree.insert_node(5)
my_tree.insert_node(3)
my_tree.insert_node(7)
my_tree.insert_node(2)
my_tree.insert_node(3)
my_tree.insert_node(8)
my_tree.insert_node(10)



#search the node
print(my_tree.search_node(11))





#print the values in the node
print(my_tree.root.data)
print(my_tree.root.right.data)
print(my_tree.root.left.data)
print(my_tree.root.left.left.data)
print(my_tree.root.right.right.data)
print(my_tree.root.left.right.data)
print(my_tree.root.left.left.data)
print(my_tree.root.right.right.right.data)
print(my_tree.root.right.right.right.right.data)




