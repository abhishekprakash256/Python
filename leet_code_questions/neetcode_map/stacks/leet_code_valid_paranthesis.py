"""
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

	Open brackets must be closed by the same type of brackets.
	Open brackets must be closed in the correct order.
	Every close bracket has a corresponding open bracket of the same type.

"""

#test cases
s = "{}{}{}"
out = True

s2 = "[[{}]]"
out2 = True

s3 = "{[]]}"
out3 = False

s4 = " "
out4 = True

s5 = "]{}"
out5 = False

s6 = "(]"
out6 = False

s7 = "(("
out7 = False

s8 = "(){}}{"
out8 = False



class Solution:
	def isValid(self,s):
		"""
		The function takes the string and check for the correct paranthesis order 
		Args:
			s: (str) The string that needs to be checked 
		Returns:
			True or False: (bool) The result string is True or False
		"""
		
		mapper = {"}":"{","]":"[",")":"("}
		stack = []
		i = 0 
		length = len(s)
		open_braces = 0
		close_braces = 0
		
		if len(s)%2 !=0:
			return False

		if s[0] == "}" or s[0] == ")" or s[0] == "]":
			return False

		while i < length:

			if s[i] == "{" or s[i] == "[" or s[i] == "(": 
				open_braces +=1
				stack.append(s[i])

			elif s[i] == "}" or s[i] == ")" or s[i] == "]":
				if len(stack) == 0:
					return False
				pop_ele = stack.pop()
				match  = mapper[s[i]]
				close_braces +=1

				if pop_ele != match:
					return False

			i+=1
		if open_braces == close_braces:
			return True
		else:
			return False
		

sol = Solution()
res = sol.isValid(s2)

print(res)