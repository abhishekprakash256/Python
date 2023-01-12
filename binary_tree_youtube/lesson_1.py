"""
implement the DFS using the stack in the python from scratch
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

def dfs_tree(root):
	"""
	The function to print the tree node using the DFS 
	by using the stack data structure
	Args:
		temp : (node) the root node of the tree
	Return:
		data : (int) The data of the node
	"""

	#implement a stack using the list 

	stack = []
	temp = root
	stack.append(temp.data)

	while len(stack) != 0 :
		if temp.left is not None and temp.right is not None:
			stack.append(temp.right)
			stack.append(temp.left)
			print(temp.data)

		elif temp.left is None and temp.right is not None:
			stack.append(temp.right)
			print(temp.data)

		elif temp.right is not None and temp.left is None:
			stack.append(temp.left)
			print(temp.data)
	
		else:
			print(temp.data)

		temp = stack.pop()



	return "Done Printing"


if __name__ == '__main__':
 	res = dfs_tree(root)
 	print(res)