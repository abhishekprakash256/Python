"""
The binary tree problem 
"""

#create a binary tree friom scratch 

class Node:
	def __init__(self,data):
		self.data = data
		self.left = None
		self.right = None



#create the tree 

root = Node(10)
node1 = Node(11)
node2 = Node(2)
node3 = Node(3)

#connect the nodes

root.right = node1
root.left = node2
root.left.right = node3

#print the tree ---------------

