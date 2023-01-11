"""
The tree insertion
using the recursion
"""

#make a tree

class Node:
	def __init__(self,data):
		self.data = data
		self.left = None
		self.right = None


#make the tree

root = Node(10)
node1 = Node(11)
node2 = Node(12)
node3 = Node(14)
node4 = Node(2)

root.left = node4
root.right = node1
node1.right = node2
node2.right = node3


#----------print the tree ------------------

print(root.data)
print(root.left.data)
print(root.right.right.right.data)


#-----------------------the function to insert the data ------------

def insert_data(root,data):
	"""
	The function to add the data in the tree
	Args:
		data: (int) The data to insert on the tree
	"""


	if root.left is None and root.right is None or root is None:
		node = Node(data)
		root = node

	elif root.data > data:
		root.left = insert_data(root.left,data)
	else:
		root.right = insert_data(root.right,data)


insert_data(root,5)

#print(root.left.data)
print(root.right.data)
print(root.right.right.data)
#print(root.right.left.data)
#print(root.left.left.data)
#print(root.right.right.right.data)