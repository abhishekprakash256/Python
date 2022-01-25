str_1 = input("Enter the string to check: ")

#input and output
'''
"abcabcbb"       -  3 -> "abc"  correct  [['a', 'b', 'c'], ['b', 'c']]
"bbbbb"         -   1  ->  "b" correct
"pwwkew"         -   3  -> "wke" incorrect
 ""             -    0  ->  ""   error


'''

def check_in_lst(x,list):       #function for the checking inside the sting 
	check = 0
	for i in list:
		if i == x:
			check =1
	return check				

#a lenth of strings and also a name to make a comparision, use a counter that will check for the 

def lengthOfLongestSubstring(check):  #main function for checking for the sub string in string 
	lst= []
	for i in check:
		if i == '"':
			continue
		else:
			lst.append(i)
	lst_3=[]   #for storing the substring
	lst_2 = [] #for storing the elements that are new and checking
	for i in range(0,len(lst)):
		if check_in_lst(lst[i],lst_2) == 0:
			lst_2.append(lst[i])
			print(lst_2)
		else:
			print(i)
			lst_2= []	

	'''lst_4 = []	
	print(lst_3)	
	for j in lst_3:                 #this line is giving error
		#print(j)
		lst_4.append(len(j))
	
	lst_4.sort()
	#print(lst_4)
	
	return lst_4[len(lst_4)-1]	'''




	

print(lengthOfLongestSubstring(str_1))

'''x= [['h', 'f', 'j'], ['h', 'j', 'g', 'k']]

for i in x:
	print(len(i))'''





'''def lengthOfLongestSubstring(check):  #main function for checking for the sub string in string 
	lst= []
	for i in check:
		if i == '"':
			continue
		else:
			lst.append(i)
	lst_3=[]   #for storing the substring
	lst_2 = []
	for i in range(0,len(lst)):
		if check_in_lst(lst[i],lst_2) == 0:
			lst_2.append(lst[i])
			#print(lst_2)
		else:
			lst_3.append(lst_2)
			lst_2= []
			lst_2.append(lst[i])
	lst_4 = []	
	print(lst_3)	
	for j in lst_3:                 #this line is giving error
		#print(j)
		lst_4.append(len(j))
	
	lst_4.sort()
	#print(lst_4)
	
	return lst_4[len(lst_4)-1]'''	
