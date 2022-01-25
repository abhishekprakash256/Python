'''Given a string s, return the longest palindromic substring in s.
Input: s = "babad"
Output: "bab"
Note: "aba" is also a valid answer.
Example 2:

Input: s = "cbbd"
Output: "bb"

Example 3:

Input: s = "a"
Output: "a"

Example 4:

Input: s = "ac"
Output: "a"
'''
'''
case_1 - if the length of the number is one print the number
case_2 - if no any palindrome string then print the first number
Algo - first check the length of the given string 
resest, passing and checking for the palindrome
make empty lst of palindrome string:
sort it per length and give the output
#make a palidrome checking function
problems - 
can simgle palindrome
multiple palindrome in the string
check a single string in the list
append it
abbcbbdb
do a nested loop and cut off


	lst_pal = []
	check_str= []
	for i in string:
		check_str.append(i)


	function(snipts):
		if snipts == snipts.reverse():
			return true
		else :		
			return false



	if len(check_str) == 1 :
		return string
	elif len > 1 :
		while len(lst_pal)<= len(check_str):
			if function(check_str[i]) == 0:
				lst_pal.append(check_str[i])
				i+=1
			else: 
				i+=1

		return	lst_pal

'''


#-------------------------checking for the pallindrome part ------------------------------------------------#

input_1 = "babad"
input_2 = "cbbd"
input_3 = "a"
input_4 = "ac"


#the making the check function
def check_pal(snips):
	if snips == snips.reverse():
		return 1
	else:
		return 0

#to make the check function part in the main func
def main_fun(string):
	str_lst = []
	
	#append in the lst
	for i in string:
		str_lst.append(i)
	pal_lst = []
	for i in range (0,len(str_lst)):
		pal_sub_lst=[]
		
		for j in range(0,i):
			pal_sub_lst.append(str_lst[j])
			#print(pal_sub_lst)
			
			if check_pal(pal_sub_lst) == 1: 
				pal_sub_lst.append(str_lst[j])
			else:
				continue 

		pal_lst.append(pal_sub_lst)
			













	return pal_lst  #change the return later







print(main_fun(input_2))














		


