"""

You are given the head of a singly linked-list. The list can be represented as:
"""

#test cases

# Definition for singly-linked list.
class ListNode:
	def __init__(self, val=0, next=None):
		self.val = val
		self.next = next


head = ListNode(1)
node1 = ListNode(2)
node2 = ListNode(3)
node3 = ListNode(4)
node4 = ListNode(5)

head.next = node1
node1.next = node2
node2.next = node3
node3.next = node4



def listPrint(node):
	temp = node
	while True:
		print(temp.val)
		if temp.next == None:
			break

		temp = temp.next

	return "Print Done"


class Solution:
	def reorderList(self,node):
		lst = []
		temp = node
		while True:
			
			lst.append(temp.val)
			if temp.next is None:
				break
			temp = temp.next

		alt = False
		head = False
		i = 0
		length = len(lst) - 1
		new_lst = []

		while i <= length:

			if head == False:
				first = lst.pop(0)
				new_lst.append(first)
				head = True

			elif alt == False:
				last = lst.pop()
				new_lst.append(last)
				alt = True

			else:
				first = lst.pop(0)
				new_lst.append(first)
				alt = False
			i+=1

		return new_lst


sol = Solution()
res = sol.reorderList(head)
print(res)