"""
The tree sum problem finding the sum of the all nodes of the tree
using the iterative and recursive approach

"""



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


def tree_sum_recursive(root)->sum:
	"""
	The program to find the sum of the all nodes of the tree
	Args:
		root: (node) The root node of the tree
	Returns:
		sum: (int) The sum of the nodes of the tree 
	"""

	if root.left is None and root.right is None:
		return root.data 
	elif root.left is not None and root.right is not None:
		return tree_sum_recursive(root.left) + tree_sum_recursive(root.right) + root.data
	elif root.left is not None and root.right is None:
		return tree_sum_recursive(root.left) + root.data
	elif root.right is not None and root.left is None:
		return tree_sum_recursive(root.right) + root.data

if __name__ == '__main__':
	res = tree_sum_recursive(root)
	print(res)