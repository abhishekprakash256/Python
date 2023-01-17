"""
The valid pallindrome problem 
"""

letter_map = {"a":True,"b":True,"c":True,"d":True,"e":True,"f":True,"g":True,"h":True,"i":True,"j":True,"k":True,"l":True,"m":True,"n":True,"o":True,"p":True,"q":True,"r":True,"s":True,"t":True,"u":True,"v":True,"w":True,"x":True,"y":True,"z":True,0:True,1:True,2:True,3:True,4:True,5:True,6:True,7:True,8:True,9:True}


#test cases
s0 = "A man, a plan, a canal: Panama"
s1 = ""
s2 = "   "
s3 = 'the fast car'






def check_valid_pallindrome(s:str)->bool:
	"""
	The valid pallindrome check function takes the string s and checks for the string valid or not 
	Args:
		s:(str) The string to check for the valid pallindrome
	Returns:
		True or False: (bool) The string is pallindrome or not return True or False
	"""
	left = 0 
	right = len(s) - 1

	while left <=right:

		if s[left] not in letter_map or s[right] not in letter_map:
			pass