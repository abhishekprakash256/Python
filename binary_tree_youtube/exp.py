"""
test for the stack
"""

stack = []

stack.append(2)
stack.append(12)
stack.append(23)
stack.append(21)
stack.append(25)


print(stack)

while len(stack)!=0:
	temp = stack.pop()
	print(temp)