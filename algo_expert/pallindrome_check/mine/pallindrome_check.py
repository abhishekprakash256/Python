'''
write a function to check a given string is pallindrome or not

'''

#test cases 

test_0 = "abcbad" #passed

test_1 = "aaaaaa"  #passed

test_2 = "abcba"  #passed

test_3 = "abcbadd"  #passed 

test_4 = "bbbcbbb"  #passed

test_5 = "bcbcbcb" #passed


def pallindrome_check(string : str) -> str:
	'''
	The function checks for the string to be pallindrome or not pallindrome

	Arguments:
		string (str) - The string input that is needed to be checked

	Returns:

		result (str) - The statement if a string is pallindrome or not 

	'''

	
	#initilaize the two pointers 

	left = 0 

	right = len(string) - 1

	#start the loop

	while left < right :

		if string[left] == string[right]:  #condidition check 

			right -=1 #increase the right pointer

			left +=1 #decrease the left pointer

		else:  #if condition fails just return

			return "The strig is not pallindrome"

	#all passesed return string is pallindrome

	return "The string is pallindrome"


print(pallindrome_check(test_5))