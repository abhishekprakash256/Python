"""
The tree min value problem 
find the min value in the tree and return it
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


def min_tree_dfs(root):
	"""
	The program to find the min of the tree
	Args:
		root: (node) The root node of the tree
	Returns:
		sum: (int) The sum of the nodes of the tree 
	"""

	stack = []
	stack.append(root)
	min_val = root.data

	while len(stack) !=0:

		temp = stack.pop()
		temp_min = temp.data

		if temp_min <= min_val:
			min_val = temp_min

		if temp.right is not None and temp.left is not None:
			stack.append(temp.right)
			stack.append(temp.left)

		elif temp.left is not None and temp.right is None:
			stack.append(temp.left)

		elif temp.right is not None and temp.left is None:
			stack.append(temp.right)

	return min_val



def min_tree_bfs(root):
	"""
	The program to find the min of the tree
	Args:
		root: (node) The root node of the tree
	Returns:
		sum: (int) The sum of the nodes of the tree 
	"""

	queue = []
	queue.append(root)
	min_val = root.data

	while len(queue) !=0:

		temp = queue.pop(0)
		temp_min = temp.data

		if temp_min <= min_val:
			min_val = temp_min

		if temp.right is not None and temp.left is not None:
			queue.append(temp.left)
			queue.append(temp.right)

		elif temp.left is not None and temp.right is None:
			queue.append(temp.left)

		elif temp.right is not None and temp.left is None:
			queue.append(temp.right)

	return min_val


def min_tree_recursive(root):
	"""
	The program to find the min of the tree using the recursive algorithm
	Args:
		root: (node) The root node of the tree
	Returns:
		sum: (int) The sum of the nodes of the tree 
	"""
	if root is None:
		return float('inf')
	left_min = min_tree_recursive(root.left)
	right_min = min_tree_recursive(root.right)

	return min(root.data,left_min,right_min)






if __name__ == '__main__':
	res0 = min_tree_dfs(root)
	res1 = min_tree_bfs(root)
	res2 = min_tree_recursive(root)
	print(res0)
	print(res1)
	print(res2)