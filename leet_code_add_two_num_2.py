'''prommpt 
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.

Example 2:

Input: l1 = [0], l2 = [0]
Output: [0]

Example 3:

Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
Output: [8,9,9,9,0,0,0,1]
'''

#my approach---------------------------------------
''' make a empty lst for sum
make loop for the largest number
add the number and keep track of the carry 
and add the carry to other number as possible 
--note laslty append the carry part as in lst'''

num_1=[]
num_2=[]

num_1 = list(map(int, input('Enter Numbers : ').split()))
num_2 = list(map(int, input('Enter Numbers : ').split()))


def the_sum(num_1,num_2):
	l1 = len(num_1)
	l2 = len(num_2)
	sum_lst=[]  #empty list that will take the sums
	carry =0  #carry for the sum of the two numbers
	if l1=l2:  #checking the length of the two nums given 
		for i in range(0,l2): #range of the smaller number
			
			add_num = num_2[l2-i-1] + num_1[l1-i-1] + int(carry) #two number are added and carry is also added
			add_num = str(add_num)
			if len(add_num)>1:       #check for the carry part
				carry = add_num[0]      #carry is initilaized
				sum_lst.append(add_num[1])   #first number appened 
			else:

				sum_lst.append(add_num)  #if carry is zero or less than two digit append the number 




	elif l1>l2:
		for i in range(len(l2)):
			add_num = num_2[l2-i-1] + num_1[l1-i-1] + int(carry) #two number are added and carry is also added
			add_num = str(add_num)



		



	sum_lst.reverse()


	if carry == 0:
		return 	sum_lst
	else: 


		return sum_lst.append(carry)
	


	


	

print(the_sum(num_1,num_2))