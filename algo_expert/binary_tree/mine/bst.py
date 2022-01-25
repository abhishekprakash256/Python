'''
construction of a BST using the oops in pyhthon
method it should support - insertion, seraching and deletion
deletion will have 3 cases , no child root - just remove, main root - replace with left most samll value 
3 case - 2 child nodes - replace with the left tree max value or replcae with the right tree subtree max value
'''

class BST():
	'''
	The BST takes node and assign to the left or the right node
	methods - 
		insertion: insert a node to the tree 

		search : search a value in the tree

		deletion: delete a node in the tree

	'''
	lst = [] #for storing the elements
	lst_2 = []
	lst_3 = []
	def __init__(self):
		self.root = None
		self.left = None 
		self.right = None
		


	def insertion(self,data):
		self.next = next
		self.data = data
		'''
		insert the value in the tree

		-----------------------------------
		Arguments:
			data: integer , the value for the data
		'''

		#start loop

		while True:


		#check for empty node

			if self.root is None:
				self.root  == 0

				#checking for the right tree
				if self.data >= self.root:
					self.next == self.right
					self.right == self.root
					self.lst_2.append(self.root)

				#checking for the left tree
				elif self.data < self.root:
					self.next == self.left
					self.left == self.root
					self.lst_3.append(self.root)

				#setting the root node
				else: 
					self.root = self.data
					self.lst.append(self.data)
					break
				




		return self.lst , self.lst_2 , self.lst_3




tree = BST()
(tree.insertion(2))
(tree.insertion(1))
(tree.insertion(3))
(tree.insertion(8))
(tree.insertion(0))
print(tree.insertion(4))
