"""
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

"""

#test cases 

n0 = 3 
out0 = ["((()))","(()())","(())()","()(())","()()()"]

n1 = 1
out1 = ["()"]


class Solution:
	def generateParenthesis(self, n: int):
		"""
		The function generate the combination of the paranthesis
		Args:
			n : (int) the count of the combinations need to be generated
		Return:
			combo_lst: (list) the list of the parranthesis combinations

		"""
		stack = []
		open_braces = 0 
		close_braces = 0
		left = 0 

		
