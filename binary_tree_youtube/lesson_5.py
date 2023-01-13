"""
find the elemenet in the tree 
using the BFS and DFS
both iterative abd recursive
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

def find_element_DFS_iterative(root,target:int)->bool:
	"""
	The funciton to find the element in the tree
	Args:
		root: (node) The root node of the array
	Return:
		True or False: (Bool) The bool value for the node found or not 
	"""

	#implemnet a stack
	stack = []
	temp = root
	stack.append(root)

	while len(stack) !=0:

		temp = stack.pop()

		if temp.data == target:
			return "Found"
		
		else:

			if temp.left is not None and temp.right is not None:
				stack.append(temp.right)
				stack.append(temp.left)

			elif temp.left is not None and temp.right is None:
				stack.append(temp.left)

			elif temp.right is not None and temp.left is None:
				stack.append(temp.right)

	return "Not Found"



def find_element_DFS_recursive(root,target:int)->bool:
	"""
	The funciton to find the element in the tree
	Args:
		root: (node) The root node of the array
	Return:
		True or False: (Bool) The bool value for the node found or not 
	"""
	if root:
		if root.data == target:
			return "Found"
		return find_element_DFS_recursive(root.left,target) or find_element_DFS_recursive(root.right,target)
		
	else:
		return "Not Found"


if __name__ == '__main__':
	res0 = find_element_DFS_iterative(root,1)
	res1 = find_element_DFS_recursive(root,13)
	print(res0)
	print(res1)