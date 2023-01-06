"""
using the sorting logic to test the anagram 
"""

#test cases 
inp = "nameless"
inp2 = "salesman"


inp3 = "cat"
inp4 = "tac"



def test_anagram(word:str, word2:str)->bool:
	"""
	The function test the anagram for the and return boolean on the val
	Args:	
		word: (str) The first word to test anagram 
		word2: (str) The second word test anagram
	Return:
		True or False: (bool) the value matches results as True or False
	"""
	if len(word) != len(word2):
		return False
	sorted_word = ''.join(sorted(word))
	sorted_word2 = ''.join(sorted(word2))
	if sorted_word == sorted_word2:
		return True
	else:
		return False

if __name__ == '__main__':
	res = test_anagram(inp3,inp4)
	print(res)