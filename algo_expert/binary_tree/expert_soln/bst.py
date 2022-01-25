'''
Algo expert solution
'''

class BST:
	#constructor
	def __init__(self,value):
		self.value = value
		self.left = None
		self.right = None
		self.lst = []
		

	#insertion method in the BST

	def insert(self,value):

		#make a current node as the next pointer 

		currentNode = self #assigning the current node as self value

		while True:

			#check the left subtree

			if value < currentNode.value:

				if currentNode.left is None:
					currentNode.left = BST(value) #assignmnet 
					self.lst.append(value)
					break
				else:
					currentNode = currentNode.left  #setting the next pointer

			#check the right subtree

			else :

				if currentNode.right is None:
					currentNode.left = BST(value)  #assignmnet
					self.lst.append(value)
					break
				else:
					currentNode = currentNode.right  #setting the next pointer


		print(self.lst)  #for checking purpose

		return self


	#search method for the tree

	def search(self,value):

		currentNode = self

		while currentNode is not None:
			if value < currentNode.value:
				currentNode = currentNode.left
			elif value > currentNode.value:
				currentNode = currentNode.right
			else:
				return True

		return False


	#remove method 

	def remove(self,value, parentNode = None):

		pass



tree = BST(4)

tree.insert(1).insert(2).insert(4).insert(6).insert(8).insert(0)

print(tree.search(9))