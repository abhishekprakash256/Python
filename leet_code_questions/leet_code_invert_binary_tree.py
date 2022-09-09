"""
The problem is to invert a binary tree with the given tree

"""

#test cases - 

Input1 = [4,2,7,1,3,6,9]
Output1= [4,7,2,9,6,3,1]

Input2 = [4,2,7,1,3,6,9]
Output2 = [4,7,2,9,6,3,1]

Input3 = []
Output3 = []




# Definition for a binary tree node.
class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right

class Solution:
    def invertTree(self, root ):
    	"""
    	The fucntion takes the tree and invert it 
    	Args:
    		root (list) : the list of the node in traversal 
    	Returns:
    		invert_root (list) : the list oft the node of the tree

    	"""
    	

    	
    	return root

if __name__ == "__main__":
   node1 = TreeNode(4)
   node2 = TreeNode(2)
   node3 = TreeNode(7)
   node4 = TreeNode(1)
   node5 = TreeNode(3)
   node6 = TreeNode(6)
   node7 = TreeNode(9)

   node1.left = node2
   node1.right = node3
   node2.left = node4
   node2.right = node3
   node4.right = node2
   node5.left = node2
   node3.left = node6
   node3.right = node7
   node6.right = node3
   node7.left = node3


   print(node1.left.val)

   Soln = Solution()
   res = Soln.invertTree(node1.left.val)
   print(res)

