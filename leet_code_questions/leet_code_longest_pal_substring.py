'''
Example 1:

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

 

Constraints:

    1 <= s.length <= 1000
    s consist of only digits and English letters (lower-case and/or upper-case),
'''

string = input("Enter the string: ")
string_lst=[]
for i in string:
	if i == '"' :
		continue
	else:
		string_lst.append(i)


def to_check_pal(sequence):

	if (c==d):
		return 1
	else:
		return 0
print(to_check_pal(string_lst))	




