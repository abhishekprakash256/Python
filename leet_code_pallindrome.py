'''
To check is the string is a pallindrome or not
examples -
case 1-  121       true
case 2- -121      false
case 3-  10         false
case 4-  -101        false   
'''

to_check = input("Enter the number to check: ")

def pallindrome_check(string):
	lst= []
	for i in to_check:
		lst.append(str(i))
	#print(lst)		
	score = 0
	for i in range(0, len(lst)):
		if lst[i]==(lst[len(lst)-i-1]):
			score = score +1
		else:
			score = score -1
	#print(score)		
	if score == (len(lst)):
		return "true"
	else:
		return "false"				

print(pallindrome_check(to_check))		
