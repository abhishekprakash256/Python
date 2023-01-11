"""
the pallindrome using the recursive call

"""


inp = "ana"
inp2 = ""
inp3 = "a"
inp4 = "ananana"
inp5 = "cat"

def check_pal(word:str)->str:
	"""
	To check the given string is a pallindrome or not
	Args:
		word: (str) The word to test the pallindrome for 
	Return:
		True or False: (bool) the word is pallidrome or not
	"""
	print(word)
	if len(word) < 2:
		return True
	else:
		if (word[0]) == (word[len(word)-1]):
			return check_pal(word[1:(len(word)-1)])
		
	return False


print(check_pal(inp5))