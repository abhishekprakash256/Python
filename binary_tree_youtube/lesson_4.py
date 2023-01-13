"""
Binary tree BFS problem
using the queue algorithm
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


def bfs_tree(root):
	"""
	The function for the bfs traversal of the tree 
	Args:
		root: (node) The root node of the tree
	Return:
		Done: (str) The string that printing is done 
	"""
	queue = []
	temp = root
	queue.append(temp)

	while len(queue) > 0:

		temp = queue.pop(0)
		
		if temp.left is not None and temp.right is not None:
			queue.append(temp.left)
			queue.append(temp.right)
		elif temp.left is not None and temp.right is None:
			queue.append(temp.right)
		elif temp.right is not None and temp.left is None:
			queue.append(temp.left)

		print(temp.data)


		
		

if __name__ == '__main__':
	res = bfs_tree(root)
	print(res)