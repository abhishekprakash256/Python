"""
using the exceptions in the program 
there are differnt types of the error that can be handled in different ways for the system 
"""

x = -5

"""
if x < 0:
	raise Exception("x should be positive")

y = -6

assert (x >=0), "x is not positive"
"""

try:
	a = x / 0
except Exception as e:
	print(e) 