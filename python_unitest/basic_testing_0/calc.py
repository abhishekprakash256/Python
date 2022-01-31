"""
the file is used for the unitesting in python code
"""
def add(a,b):

	return a + b

def sub(a,b):

	return a - b


def mul(a,b):

	return a * b


def divide(a,b):

	if b == 0:
		raise ValueError("Can't divide by zero!")

	return a / b

def remain(a,b):

	return a % b
