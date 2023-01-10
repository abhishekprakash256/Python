"""
The recursion starting\
the program to make the string revere using the recursion 
"""

inp = "hello"

def reverse_string(inp:str)->str:
	"""
	The function takes the string and reverese the string 
	Args:
		inp: (str) The input string 
	Return:
		reverse_str: (str) The output string of the string reversed
	"""
	#base case 


	#what to do in each iteration

	if len(inp) == 0:
		return ""

	else:
		rev_string = ""
		#reverse_string(inp[0:len(inp)-1])
		return rev_string + reverse_string(inp[0:len(inp)-1])

print(reverse_string(inp))