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

def check_deficit(num_1,num_2):
	if len(num_1) == len(num_2) :
			num_1,num_2
	elif len(num_1) > len(num_2) :
		for i in range(0, (len(num_1)- len(num_2))):
			num_2.insert(0,0)
		
	else :
		for i in range(0 , (len(num_2)- len(num_1))):
			num_1.insert(0,0)

	print("The number 1 is " ,num_1)
	print("The number 2 is ", num_2)
		
	num_1.reverse(), num_2.reverse()
	return num_1, num_2

#add the logic for the carry part
def main_add(num_1,num_2):
	check_deficit(num_1,num_2)
	carry = 0
	sum= 0
	add_lst =[]
	for i in range(0,len(num_2)):
		sum = num_1[i]+num_2[i] + carry
		sum = str(sum)
		if len(sum)> 1:
			add_lst.append(int(sum[1]))
			carry = int(sum[0])
		else:
			add_lst.append(int(sum))	

	add_lst.append(carry)
	add_lst.reverse()
	

	return add_lst













print(main_add(num_1,num_2))