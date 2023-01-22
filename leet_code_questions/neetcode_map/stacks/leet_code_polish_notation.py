"""
You are given an array of strings tokens that represents an arithmetic expression in a Reverse Polish Notation.

Evaluate the expression. Return an integer that represents the value of the expression.

Note that:

    The valid operators are '+', '-', '*', and '/'.
    Each operand may be an integer or another expression.
    The division between two integers always truncates toward zero.
    There will not be any division by zero.
    The input represents a valid arithmetic expression in a reverse polish notation.
    The answer and all the intermediate calculations can be represented in a 32-bit integer.
"""


#test case 

tokens0 = ["2","1","+","3","*"]
out0 = 9 

tokens1 = ["4","13","5","/","+"]
out1 = 6

tokens2 =  ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
out2 = 22

tokens3 = ["1","3","+"]
out3 = 4

tokens4 = ["18"]
out4 = 18


class Solution:
	def evalRPN(self,tokens)->int:
		"""
		The function evaluate the RPN based on the symbols
		Args:
			tokens: (list) the list of the numbers and the symbols
		Return:
			cal: (int) the value of the calulated integers based on the symbols
		"""

		stack = []
		left = 0 
		length = len(tokens) 
		symbol = ("*","/","-","+")


		while left < length:

			if tokens[left] not in symbol:
				stack.append(tokens[left])
			else:
				
				first = int(stack.pop())
				second = int(stack.pop())
				
				if tokens[left] == "*":
					cal = second * first
				
				elif tokens[left] == "/":
					cal = second / first

				elif tokens[left] == "+":
					cal = second + first

				elif tokens[left] == "-":
					cal = second - first 

				stack.append(cal)

			left+=1

		return int(stack.pop())

sol = Solution()
res = sol.evalRPN(tokens4)

print(res)  