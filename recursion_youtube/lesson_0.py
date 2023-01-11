"""
The recursion starting\
the program to make the string revere using the recursion 
"""

inp = "hello"
inp2 = "Sashimi"
inp3 = "Chai"


def reverse_string(word:str)->str:
	"""
	The function takes the string and reverese the string 
	Args:
		inp: (str) The input string 
	Return:
		reverse_str: (str) The output string of the string reversed
	"""
	#base case 


	#what to do in each iteration

	if len(word) == 0:
		return ""
	else:
		return word[len(word)-1]+reverse_string(word[0:len(word)-1])

print(reverse_string(inp))