"""
The function takes the string and removes all the repatative character
Chapter 2 , Question 3

ball bat - bat l

"""



def remove_duplicate(string: str)-> str:
	"""
	The function will take string and remove the duplicate values
	Arguments:
		string (str) -> the string to check for the repetative values

	Returns:

		string (str) -> the string with only one values
	"""

	new_str = ""

	looked_values = {}

	for i in string:

		if i not in looked_values:

			looked_values.update({i:True})

			new_str +=i 


	return new_str

print(remove_duplicate("ball bat"))








