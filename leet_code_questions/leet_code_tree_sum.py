"""
The sum of the tree node that is equal to the root 

4<-10->6
sum is 10, so return True

The tree consists only of the root, its left child, and its right child. 
"""

#test cases 

Input = [10,4,6]
Output = True


Input2 = [5,3,1]
Output2 = False

#Definition for a binary tree node.
class TreeNode:
 def __init__(self, val=0, left=None, right=None):
	 self.val = val
	 self.left = left
	 self.right = right


class Solution:
	def checkTree(self, root) -> bool:
		"""
		The function takes the root value and checks the node and add the value of the children 
		to check the root value 

		Args:
			root (list) : the list of the node that are in the tree
		Returns:
			True or False (bool) : the bool value of the sum true or false
		"""

		if root.val == root.left.val + root.right.val:
			return True
		else:
			return False 
		


if __name__ == "__main__":
   node1 = TreeNode(10)
   node2 = TreeNode(4)
   node3 = TreeNode(6)
   node1.left = node2
   node1.right = node3
   node2.right = node1 
   node3.left = node1


   Soln = Solution()
   
   res = Soln.checkTree(node1)
   print(res)
