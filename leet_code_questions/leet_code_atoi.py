'''
read and ignore white space
for + result is positive and - result is negative if nothing its +ve
ignore any non-digits and read the strings
maintain a range of -2^31 to 2^31 -1 check for the range as well
after " we have to get white space or "-" or "+" or any digit any non digit the reading is stopped

--------------------------------------------------------------------------------
example 
1. input = "42" outut is 42
2. input = "    -42"  output is -42
3. input = "4193 with words" output is 4193
4. input = "words and 987" output is 0
5. input = "-91283472332" output is -2147483648'''

def myAtoi(string):
	lst =[]
	new_str= (string.replace(" ", "")) 
	for i in new_str:
		if i == '"':
			continue
		else:
			lst.append(i)
	#print(lst)		
	lst_2 =[]		
	for i in lst:
		if i == 0:

			if i != x or i != "+" or i !="-":
				return 0
		else:		
			
			if i == "-":
				lst_2[0]= "-"
			elif i == "+" or i!="1" or i!="2" or i!="3" or i!="4" or i!="5" or i!="6" or i!="7" or i!="8" or i!="9" or i!= "0" :
				continue
			else:	
				lst_2.append(str(i))
				
	
					

    

	
	return lst_2

print(myAtoi("+67  abdf"))