"""
The solution of the qurestion sum in the linked list
using the class soln
"""


#Test cases

l1 = [1,0,0]
l2 = [0]  #000

l3 = [1,1,1,1]
l4 = [1,1]  #2211


l5 = [9,9]
l6 = [9,0] #801


l7 = [9,9,9]  
l8 = [9,9] #

l9 = [9,9,8]
l10 = [7]





# Definition for singly-linked list.
class ListNode:
	 def __init__(self, val=0, next=None):
		 self.val = val
		 self.next = next

class Solution:
	def __init__(self):
		self.head = None
	def addTwoNumbers(self, l1: [ListNode], l2: [ListNode]) -> [ListNode]:
		"""
		The addition of the two numbers from the linked list 
		Args
			l1 (linked node): The list node of the linked list
			l2 (linked node): The list node of the linked list
		Returns:
			out (linked list): The linked lis of the added numbers 
		"""
		#make a new node 
		new_node = ListNode()

		carry = 0

		digit = 0

		for i in l1:
			print("the value of i",i)

			curr = new_node

			if self.head is None:
				curr = self.head
				self.head = new_node
				self.head.val = i
				print("the head next", self.head.next)
				print("inside", self.head.val)
			else:
				curr.val = i
			
			print("in")


		print("the head val is ",self.head.val)


	def  print_lst(self,val):
		"""
		The function is used to print the linked list
		"""

		curr = ListNode(val)

		while True:
			if curr.next is None:
				print(curr.val)
				break

			print(curr.val)

			curr = curr.next




if __name__ == '__main__':
	soln = Solution()
	print(soln.addTwoNumbers(l1,l2))

