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
'''
my approah - first check the legth of the number 
if same implement the same logic for carry and addition
#------------------------------
if not same add the number of 0 as the equivalent to the length of the number
then make the addition and do as given
reverse in last
'''


num_1=[]
num_2=[]

num_1 = list(map(int, input('Enter Numbers : ').split()))
num_2 = list(map(int, input('Enter Numbers : ').split()))


def the_sum(num_1,num_2):
	l1 = len(num_1)
	l2 = len(num_2)
	
	#to check the length of the number and if equal good or add the numbers of zeros

	

	

	#---------------------------the addition part of the numbers--------------------------------------------#
	sum_lst=[]  #empty list that will take the sums
	carry =0  #carry for the sum of the two numbers
	add_num = 0
	#simple sum part for non carry implementation
	if (l1==l2):
		num_1 = num_1
		num_2 = num_2
		for i in range(0, l2):
			add_num = num_1[i]+num_2[i] + int(carry)
			
			add_num = str(add_num)

			if len(add_num)==1:
				sum_lst.append(int(add_num))
			else:
				carry = add_num[0]      #carry is initilaized
				sum_lst.append(int(add_num[1]))

	elif (l1< l2) :
		for i in range(0,l2-l1):
			num_1.append(0)
		num_1.reverse()

	else:
		for i in range(0, l1-l2):
			num_2.append(0)	
		num_2.reverse()
	







		

	return sum_lst















print(the_sum(num_1,num_2))


