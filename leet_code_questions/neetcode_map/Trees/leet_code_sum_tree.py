"""
to find the sum of the tree 
"""

#make the node 
class Node:
	def __init__(self,val):
		self.val = val 
		self.left = None
		self.right = None




class Solution:
	def sum_tree(self,root):
		"""
		Find the sumo of the tree
		"""

		#make the recursive soltion 

		if root is None:
			return 0 

		return root.val + self.sum_tree(root.left) + self.sum_tree(root.right)





if __name__ == "__main__":
	root = Node(1)
	node1 = Node(2)
	node2 = Node(3)
	node3 = Node(4)

	#connect the node

	root.left = node1 
	root.right = node2
	node2.right = node3


	sol = Solution()
	sum = sol.sum_tree(root)
	print(sum)
