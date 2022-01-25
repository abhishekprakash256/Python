"""
The number is divisible by 3 print foo and if divisible by 7 print bar
Chapter 1, Q - 38

"""

def print_foo_bar():
	"""
	The function will print foo and bar 
	if divisible by 3 foo 
	if divisible by 7 bar

	Return:
		foo, bar (string) - the messgae when number is divisible
	"""

	for i in range(100,201):

		if i % 3 == 0 and i % 7:

			print("FooBar")



print(print_foo_bar())

