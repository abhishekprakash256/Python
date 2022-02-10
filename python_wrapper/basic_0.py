"""
The file contains the impelentation of the wrapper in python

"""

#the outer function
def outer_function():
	message = "hi"

	#the inner function
	def inner_function():
		print("message")

	return inner_function()


#the calling of the function
out = (outer_function())