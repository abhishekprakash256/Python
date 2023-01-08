"""
The program to check the tree are symetric are not 
"""

#program to make a tree

class Node():
	def __init__(self,data):
		self.data = data 
		self.left = None
		self.right = None


#make the first tree
root0 = Node(7)
root0.left = Node(3)
root0.right = Node(4)
root0.left.left = Node(2)
root0.left.right = Node(5)


#make the second tree
root1 = Node(7)
root1.left = Node(4)
root1.right = Node(3)
root1.right.left = Node(5)
root1.right.right = Node(2)



#------------------to check the tree are symetric or not 

def are_symetric(root1,root2):
	if root1 is None and root2 is None:
		return True
	elif (root1 is None) != (root2 is None) or root1.data != root2.data:
		return False
	else:
		return are_symetric(root1.left,root2.right) and are_symetric(root1.right,root2.left)


def isMirror(root1, root2):
	# If both trees are empty, then they are mirror images
	if root1 is None and root2 is None:
		return True

	if (root1 is not None and root2 is not None):
		if root1.data == root2.data:
			return (isMirror(root1.left, root2.right)and
					isMirror(root1.right, root2.left))

	return False



#-------------print the tree recursively 

def tree_priter0(node):
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
		tree_priter0(node.right)
	elif node.right is None and node.left is not None:
		print(node.data)
		tree_priter0(node.left)
	else:
		print(node.data)
		tree_priter0(node.left)
		tree_priter0(node.right)


def tree_priter1(node):
	"""
	The function prints the treein DFS
	Args:
		node: (tree-node) The root node of the tree
	Return:
		data: (int) The integer values of the node
	"""
	if node.left is None and node.right is None:
		print(node.data)
	elif node.right is None and node.left is not None:
		print(node.data)
		tree_priter1(node.left)
	elif node.left is None and node.right is not None:
		print(node.data)
		tree_priter1(node.right)
	else:
		print(node.data)
		tree_priter1(node.right)
		tree_priter1(node.left)




if __name__ == '__main__':
	#print(tree_priter0(root0))
	#print(tree_priter1(root1))
	print(are_symetric(root0,root1))
	print(isMirror(root0,root1))
