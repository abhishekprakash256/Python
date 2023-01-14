"""
to find the elemnt in the tree using the BFS search
iterative and recursive appoach
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

def find_element_bfs_iterative(root,target:int)->bool:
	"""
	The funciton to find the element in the tree
	Args:
		root: (node) The root node of the array
	Return:
		True or False: (Bool) The bool value for the node found or not 
	"""
	queue = []
	temp = root
	queue.append(temp)

	while len(queue)!=0:

		temp = queue.pop(0)

		if temp.data == target:
			return "Found"

		else:
			if temp.right is not None and temp.left is not None:
				queue.append(temp.left)
				queue.append(temp.right)
			elif temp.right is not None and temp.left is None:
				queue.append(temp.right)
			elif temp.left is not None and temp.right is None:
				queue.append(temp.left)

	return "Not Found"


if __name__ == '__main__':
	res0 = find_element_bfs_iterative(root,12)
	print(res0)
