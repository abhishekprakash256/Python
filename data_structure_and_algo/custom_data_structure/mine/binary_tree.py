'''
make the binary tree data struttue in poython that has key and left right attribute 
make the node and the tree data structure
have to have methods like - insert , traverse, find

later method- delete , update
'''

#make the node class

class Node: 

	'''
	The node class that has key and the left and right method
	'''

	def __init__(self,data):
		self.key = data
		self.left = None
		self.right = None


class Tree:
	'''
	The tree class has two methods the insert and the find 
	that traverse though the node and insert the elements
	first set the head to none 
	'''

	def __init__(self):

		self.root_node = None


	def insert(self,data):

		'''
		set the root node to the key values
		the root node is set first 
		then travserse the tree and set the node, based on the comparision
		'''
		new_node = Node(data)

		if self.root_node == None:

			self.root_node = new_node

			return "Root node is set"

		else:

			temp = self.root_node

			#traverse the tree in both direction

			while True:


				if temp is None:

					#set the node here

					if previous.right is None:

						previous.right = new_node
					
					else:

						previous.left = new_node 

					break

				elif temp.key > data:

					#print("seocnd")

					#traverse right

					previous = temp

					temp = temp.right


				elif temp.key < data:

					#print("three")

					#traverese left 

					previous = temp

					temp = temp.left


			return "Node is set"

	def traverse(self):

		temp = self.root_node

		#how to traverse from the root node 

		#left -> root -> right

		#start the travere exhaust the left subtree first 

		while True:

			if temp.left is not None: #traverse the left 

				temp = temp.left

			elif temp.left is None:

				print(temp.key)

				#how to traverse the top node

				







 
		













my_tree = Tree()
print(my_tree.insert("first"))

print(my_tree.insert("second"))

print(my_tree.insert("three"))

print(my_tree.insert("four"))

print(my_tree.insert("five"))

print(my_tree.insert("six"))

print(my_tree.traverse())