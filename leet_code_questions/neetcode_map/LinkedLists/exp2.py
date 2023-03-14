"""
make the the two linked list iterartor 
"""

class Node:
	def __init__(self,val,next = None):
		self.val = val
		self.next = None



#make the first list 

head = Node(1)
node2 = Node(2)
node3 = Node(3)


head.next = node2
node2.next = node3


#make the second list

head2 = Node(1)
node22 = Node(2)
node23 = Node(3)
node24 = Node(4)
node25 = Node(5)


head2.next = node22
node22.next = node23
node23.next = node24
node24.next = node25


#the list traverser 

class Solution:
	def printer(self,head):
		"""
		print the list
		"""
		temp = head

		while True:

			print(temp.val)

			if temp.next == None:
				break

			temp = temp.next 


	def printer_two(self,head1,head2):
		"""
		Print the list
		"""

		temp1 = head1
		temp2 = head2

		while True:

			if temp1.next == None and temp2.next == None:
				print(temp1.val)
				print(temp2.val)
				break

			elif temp1.next == None:
				print(temp2.val)
				temp2 = temp2.next

			elif temp2.next == None:
				print(temp1.val)
				temp1 = temp1.next

			else:
				print(temp1.val)
				print(temp2.val)
				temp1 = temp1.next
				temp2 = temp2.next




if __name__ == "__main__":
	sol = Solution()
	#res = sol.printer(head)
	res2 = sol.printer_two(head,head2)

	print(res2)
