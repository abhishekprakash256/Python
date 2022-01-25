"""
The function to remove the jabber id of the email 

"""

test_0 = "piyush@xyz.com/qwerty"

def extract_id(email:str)-> str:
	"""
	function to extract the email id 

	Arguments :
		email (str) -> the email address with jabber id 

	Returns:
		email (str) -> the cleaned email id 
	"""

	clean_email = ""

	for i in email:

		if i == '/':

			break

		else:

			clean_email +=i


	return clean_email



print(extract_id(test_0))

