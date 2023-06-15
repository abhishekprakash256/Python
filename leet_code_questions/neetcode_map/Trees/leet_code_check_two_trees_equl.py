"""
to check the two trees are equal 
"""

#make the tree class
class node:
	def __init__(self,val):
		"""
		The function to make the node
		"""
		self.val = val
		self.left = None
		self.right = None



#make the tree 1
root = node(1)
node2 = node(2)
node3 = node(3)
node4 = node(4)

#make the other tree 2 
root2 = node(1)
node5 = node(2)
node6 = node(3)
node7 = node(4)


#connect the node of tree 1
root.left = node2
root.right = node3
node3.right = node4


#connect the node of tree 2
root2.left = node5
root2.right = node6
node6.right = node7




class Solution:
	def match_tree(self,root1,root2):
		"""
		the function to match the two trees 
		"""

		#check if thw two root exists

		if (root1.left == None and root2.left == None) or (root1.right == None and root2.right == None):
			return True

		elif root1.left.val == root2.left.val and root1.right.val == root2.right.val:
			return self.match_tree(root1.left,root2.left) and self.match_tree(root1.right,root2.right)
			
		else:
			return False

		







if __name__ == "__main__":
	sol = Solution()
	sol.match_tree(root,root2)