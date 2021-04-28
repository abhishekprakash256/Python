#Question:-
#https://leetcode.com/problems/add-two-numbers/


#test cases------------------------------------------------------------------------
check_lst = [2,4,3]
check_lst_2 = [5,6,4]  #output[8,0,7]

check_lst_3 = [0]
check_lst_4 = [0]      #output [0]


check_lst_5 = [9,9,9,9,9,9,9]
check_lst_6 = [9,9,9,9]         #output [8,9,9,9,0,0,0,1]
                   

#arr_1 = list(map(int, input().rstrip().split()))

#arr_2 = list(map(int,input().rstrip().split()))



def addTwoNumbers(l1, l2):
	#to chceck the length which one is greater
	new_lst = []  #initilaizing the empty list 
	if (len(l1) == len(l2)):                 #length iteration of the bigger list
		carry = 0
		for i in reversed(range(0, len(l1))):           #reversed used for the iteration    
			sum = 0
			sum = l1[i] + l2[i] + int(carry)               #calucaltion of the sum
			sum = str(sum)
			#print(sum)
			if (len(sum) == 1):
				carry = 0
				new_lst.append(int(sum))         #problem to tackle - list exhaustion and the sum is treated as interger

			else:
				carry = sum[0] 
				new_lst.append(int(sum[1]))


    #---------------------------make the array operation compatible with less size of the array as well-----------------------#

	else:
		if (len(l1) > len(l2)):
			carry = 0
			for i in reversed(range(0,len(l2))):
				sum = 0
				sum = l1[i] + l2[i] + int(carry)
				sum = str(sum)
				if(len(sum) ==1):
					carry = 0
					new_lst.append(int(sum))
				else:
					carry= sum[0]
					new_lst.append(int(sum[1]))

 
			for i in range(len(l2),len(l1)):
				sum = int(l1[i]) + int(carry)
				sum = str(sum)
				if (len(sum) ==1 ):
					carry =0
				else:
					carry = sum[0]
					new_lst.append(int(sum[1]))	


		else:
			for i in reversed(range(0,len(l1))):
				sum = 0
				sum = l1[i] + l2[i] + int(carry)
				sum = str(sum)
				if(len(sum) ==1):
					carry = 0
					new_lst.append(int(sum))
				else:
					carru= sum[0]
					new_lst.append(int(sum[1]))	

			for i in range(len(l2),len(l1)):
				sum = int(l1[i]) + int(carry)
				sum = str(sum)
				if (len(sum) ==1 ):
					carry =0
				else:
					carry = sum[0]
					new_lst.append(int(sum[1]))	

							
	if (carry == 0):
		return new_lst                       #reversal of the value 
	else:
		new_lst.append(int(carry))	                  #addition of the carry value		
		
	return new_lst


print(addTwoNumbers(check_lst_5,check_lst_6))







