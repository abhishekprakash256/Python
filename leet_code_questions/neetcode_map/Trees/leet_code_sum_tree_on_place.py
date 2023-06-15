"""
make the code to sum the tree on place
"""

#make the node 
class Node:
	def __init__(self,val):
		self.val = val 
		self.left = None
		self.right = None




class Solution:
	def sum_tree_on_place(self,root):
		"""
		Find the sumo of the tree
		"""

		#make the old value remeber
		










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
	sum = sol.sum_tree_on_place(root)
	print(sum)
