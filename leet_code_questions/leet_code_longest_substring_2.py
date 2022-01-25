check = str(input("Enter the string to check:"))

#element = str(input("enter the element: "))

def to_check(element, in_check_lst):
	for i in in_check_lst:
		if (element) == i:
			return 1
	
	return 0	 	
	


def sub_string(string):
	lst=[]
	for i in string:
		if i == '"':
			continue
		else:	            #appemding to the list
			lst.append(i)
	lst_2=[]                 # second list for the appending
	lst_3= []	             #thirtd list that has other lists
	for i in range(0,len(lst)):     
		if len(lst_2) == 0 :
			lst_2.append(lst[i])
		else:
			if to_check(lst[i],lst_2) == 0 :
				lst_2.append(lst[i])
				print(lst_2)
			else:
				lst_3.append(len(lst_2))
				lst_2 = []
				lst_2.append(lst[i])
	lst_3.sort()
	if len(lst_3) == 0:
		return 0
	elif len(lst_3) == 1:
		return 1	
	else:
		return lst_3[len(lst_3)-1]				





print(sub_string(check))	


# x = [0.7839,0.1243,0.0853,0.0710,0.0603,0.0562,0.0487,0.0466,0.0413,0.0405,0.0408,0.0378,0.0370,0.0318,0.0304]  
#y = [0.7601,0.9624,0.9734,0.9780,0.9819,0.9835,0.9852,0.9853,0.9870,0.9877,0.9870,0.9875,0.9881,0.9900,0.9899] 

# x_1 = [0.0831,0.0564,0.0472,0.0390,0.0394,0.0361,0.0344,0.0317,0.0320,0.0307,0.0310,0.0293,0.0272,0.0318,0.0285]
# y_1 = [0.9780,0.9830,0.9865,0.9883,0.9895,0.9897,0.9900,0.9912,0.9910,0.9918,0.9908,0.9922,0.9928,0.9902,0.9930]  