"""
path to the max 
in the tree
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


def path_max_dfs(root):
	"""
	The function to find the path to max using the recursion
	Args:
		root: (node) the root node of the tree
	Return:
		path_max: (list) the max path to the node of the tree
	"""
	max_val = root.data
	stack = []
	path = []
	stack.append(root)

	while len(stack) !=0:

		temp = stack.pop()
		temp_val = temp.data

		if temp_val >= max_val:
			path.append(temp_val)
			max_val = temp_val

		if temp.left is not None and temp.right is not None:
			stack.append(temp.left)
			stack.append(temp.right)

		elif temp.left is not None and temp.right is None:
			stack.append(temp.left)

		elif temp.right is not None and temp.left is None:
			stack.append(temp.right)

	return path


def path_max_bfs(root):
	"""
	The function to find the path to max using the recursion
	Args:
		root: (node) the root node of the tree
	Return:
		path_max: (list) the max path to the node of the tree
	"""
	max_val = root.data
	queue = []
	path = []
	queue.append(root)

	while len(queue) !=0:

		temp = queue.pop(0)
		temp_val = temp.data

		if temp_val >= max_val:
			path.append(temp_val)
			max_val = temp_val

		if temp.left is not None and temp.right is not None:
			queue.append(temp.right)
			queue.append(temp.left)

		elif temp.left is not None and temp.right is None:
			queue.append(temp.left)

		elif temp.right is not None and temp.left is None:
			queue.append(temp.right)

	return path


def path_max_recursive(root):
	"""
	The function to find the path to max using the recursion
	Args:
		root: (node) the root node of the tree
	Return:
		path_max: (list) the max path to the node of the tree
	"""
	if root is None:
		return float('-inf')
	left_min = path_max_recursive(root.left)
	right_min = path_max_recursive(root.right)
	return max(root.data,left_min,right_min)
	



if __name__ == '__main__':
	res0 = path_max_dfs(root)
	res1 = path_max_bfs(root)
	res2 = path_max_recursive(root)
	print(res0)
	print(res1)
	print(res2)