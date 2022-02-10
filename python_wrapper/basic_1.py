"""
The file contains the impelentation of the wrapper in python
with passing the function

"""

def decorator_function(original_function):
	def wrapper_function():
		print('wrapper exextued this before')

		return original_function()

	return wrapper_function

@decorator_function

def display():
	print('the function ran')

display()





"""
Links 
https://www.youtube.com/watch?v=FsAPt_9Bf3U

"""