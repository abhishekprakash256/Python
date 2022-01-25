"""
The function that counts the most occurng charater in an array 

Chapter 2 ,Question - 4
coffee cuffe

"""

def repeation_val(string: str)->int:
	"""
	The function counts the most frequent occuring character

	Arguments:
		string (str) -> the input string 

	Returns:

		freq (int) -> The most repreating character in the string
	"""
	count = {}
	for s in string:
	  if s in count:
	    count[s] += 1
	  else:
	    count[s] = 1

	for key in count:
	  if count[key] > 1:
	    print(key, count[key])


print(repeation_val("coffee cuffe"))