"""
Given the root of a binary tree, invert the tree, and return its root.
"""

root = [4,2,7,1,3,6,9]
Output = [4,7,2,9,6,3,1]


class Solution:
    def invertTree(self, root : list):
    	"""
    	The function to revert the tree from the root and return the root algo 
    	"""

    	if not root:
    		return None

    	#swap the children
    	tmp = root.left
    	root.left = root.right
    	root.right = tmp

    	#the recursive call
    	self.invertTree(root.left)
    	self.invertTree(root.right)

    	return root




# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution2:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root:
            root.left, root.right = root.right, root.left
            self.invertTree(root.left)
            self.invertTree(root.right)
        
        return root