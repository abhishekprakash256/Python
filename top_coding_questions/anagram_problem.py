"""
The problem to check if the two given strings are anagran or not 
"""

#test cases 
inp = "nameless"
inp2 = "salesman"


inp3 = "cat"
inp4 = "tac"


def test_anagram(word:str, word2:str)->bool:
	"""
	The function to test the two words are anagram or not 
	Args:
		word: (str) the first word to check the anagram
		word2: (str) the second word to check the anagram
	Return 
		True or False: (bool) either true or false the string matching or not
	"""

	if len(word) != len(word2):
		return False

	#make the two equal dict for the anagram storage with index
	first_map = {}
	second_map = {}
	for i in word:
		if i not in first_map:
			first_map[i] = 0
		first_map[i] = first_map[i] + 1

	for j in word2:
		if j not in second_map:
			second_map[j] = 0
		second_map[j] = second_map[j] +1

	#test the two dict are equal or not 
	if first_map == second_map:
		return True
	else:
		return False

if __name__ == '__main__':
	res = test_anagram(inp3,inp4)
	print(res)