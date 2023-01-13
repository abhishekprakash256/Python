"""
The DFS traverse using the recursion
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
node4 = Node(1)
node5 = Node(13)
#connect the nodes

root.right = node1
root.left = node2
root.left.right = node3
root.left.left = node4
root.right.right = node5


#print the tree ---------------

"""
print(root.data)
print(root.left.data)
print(root.left.right.data)
print(root.left.left.data)
print(root.right.right.data)

"""
#-------------------------------------


def dfs_tree_print(root):
	"""
	The function to print the tree using the recursion
	Args:
		temp : (node) the root node of the tree
	Return:
		data : (int) The data of the node
	"""
	if root :
		print(root.data)
		dfs_tree_print(root.left)
		dfs_tree_print(root.right)


print(dfs_tree_print(root))

