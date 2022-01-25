'''
recurring character fuction and return the character thar repeats 
'''

#try the opotimal approach 

test_0 = "abcbad" 
out_0 = "b"

test_1 = "abc"
out_1 = None

test_2 = "abad"
out_2 = "a"

test_3 = "dcbaba"
out_3 = "b"

test_4 = "abcbbda" 
out_4 = "b"

test_5 = "abcdcdhjk"  
out_5 = "c"


def recurring_check_2(word: str)-> str:
	'''
	The function takes the string and gives out the character that is repeated

	Arguments: 
		word (str) : the input string

	Return:

		out (str) : the repeated character  

	'''

	#optimal approach

	#create a check dict

	check_dict = {}

	#loop over the elements 

	for i in range(len(word)):

		#check the element in the dict 

		if word[i] not in check_dict:

			check_dict.update({word[i] : True})

		else:

			return word[i]

	return None



print(recurring_check_2(word = test_5))
