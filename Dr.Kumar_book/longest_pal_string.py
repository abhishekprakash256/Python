"""
The function takes the input string and returns the longest pallindrom string

Chapter 2 , Question 5

"""
test_0 = "abcbcbd" # bcbcb

test_1 = "abcbdf" # bcb

test_2 = "fcdfcfgggggh" #fcf

test_3 = "fcfhhjddd" #ddd


def check_pal(cur_string:str)-> bool:
	"""
	The function to check for the pallindrome string 
	"""

	if cur_string == cur_string[::-1]:

		return True
	else:

		return False


def longest_pallindrome(string : str) -> str:

	"""
	The function returns the longest pallindrome string 

	Arguments:
		string (str) -> the string to check the longest pallindrome
	Return:
		pall_str (str) -> the longest pallindrome string
	"""

	longest_len = 0

	for i in range(len(string)):

		for j in range(i,len(string)):

			if check_pal(string[i:j+1]) == True:

				len_of_pal = j - i

				if len_of_pal > longest_len:

					longest_len = len_of_pal

					pal_str = string[i:j+1]


	return pal_str



print(longest_pallindrome(test_0))
