"""
The program is to fimd the sum of the two linked list

example - 

2->4->3
5->6->4
-------
7->0->8

works like reversed list 
3->4->2
4->6->5
-------
8->0->7


does not have zero leading 
numbers are in the range between 0 to 100
"""

"""
The test cases are as folows:- 

l1 = [0]
l2 = [0]
out = [0]

l1 = [1,2,3]
l2 = [1,2,3]
out = [2,4,6]


l1 = [9,9,9]
l2 = [9,9,9]
out = [8,9,9,1]
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


l1 = [0,0,0]
l2 = [0]

l3 = [1,1,1,1]
l4 = [1,1]


l5 = [9,9]
l6 = [9,0]


l7 = [9,9,9]  #wrong
l8 = [9,9]

l9 = [9,9,8]
l10 = [7]

class Solution:
	def addTwoNumbers(self, l1, l2) ->list:
		self.l1 = l1
		self.l2 = l2
		#add the two number

		#to make the two list equal 
		length1 = len(l1)
		length2 = len(l2)

		if length1 > length2: 	
			bigger_len = length1
			diff = length1 - length2
			for i in range(diff):
				self.l2.append(0)
		else:
			bigger_len = length2
			diff = length2 - length1
			for i in range(diff):
				self.l1.appned(0)

		carry = 0 
		sum = 0
		digit = 0

		out = []

		#add the two numbers for the two

		for i in range(bigger_len):
			#sum logic
			sum = l1[i] + l2[i] + carry
			
			#condition for the carry and the digit 

			if 0<= sum <=9:
				carry = 0
				digit = sum

			elif 10 <= sum <=19:
				carry = 1
				digit = sum%10

			else:
				digit = 0
				carry = 20%10

			out.append(digit)

		if len(out) == bigger_len and carry !=0:
			out.append(carry)


		return out

sol = Solution()
two = sol.addTwoNumbers(l7,l8)

print(two)