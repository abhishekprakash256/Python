"""
make a tree and the traverse in the recursion 
"""

#---------------the node class ----------------
class Node:
	def __init__(self,data):
		self.data = data
		self.right = None
		self.left = None


#-------------print the tree recursively 

def tree_priter(node):
	"""
	The function prints the treein DFS
	Args:
		node: (tree-node) The root node of the tree
	Return:
		data: (int) The integer values of the node
	"""
	if node.left is None and node.right is None:
		print(node.data)
	elif node.left is None and node.right is not None:
		print(node.data)
		tree_priter(node.right)
	elif node.right is None and node.left is not None:
		print(node.data)
		tree_priter(node.left)
	else:
		print(node.data)
		tree_priter(node.left)
		tree_priter(node.right)




#------------------the tree making --------------------------
root = Node(5)
root.left = Node(4)
root.right = Node(6)
root.left.left = Node(1)
root.left.right = Node(9)
root.left.left.left = Node(3)
root.right.left = Node(10)


#print the tree-------------
"""
print(root.data)
print(root.left.data)
print(root.left.left.data)
print(root.right.left.data)
"""

print(tree_priter(root))