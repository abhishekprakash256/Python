"""
Given head, the head of a linked list, determine if the linked list has a cycle in it.

There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer. Internally, pos is used to denote the index of the node that tail's next pointer is connected to. Note that pos is not passed as a parameter.

Return true if there is a cycle in the linked list. Otherwise, return false.

"""



#Definition for singly-linked list.
class ListNode:
	def __init__(self, x):
		self.val = x
		self.next = None


head = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)
node4 = ListNode(4)

#make the list

head.next = node2
node2.next = node3
node3.next = node4
node4.next = node2



class Solution:
	def hasCycle(self,head):
		
		mapper = {}
		temp = head

		if temp == None:
			return False

		while True:

			if temp.next == None:
				return False

			if temp in mapper:
				return True
			
			mapper[temp] = True
			temp = temp.next

		return False


	def hasCycleset(self,head):

		seen = set()
		temp = head


		if temp == None:
			return False

		while True:

			if temp.next == None:
				return False

			if temp in seen:
				return True

			seen.add(temp)
			temp = temp.next

		return False


	def hasCyclepointer(self,head):
		"""
		using two pointer 
		"""

		slow = head
		fast = head 

		while fast and fast.next:

			slow = slow.next
			fast = fast.next.next 


			if slow == fast:
				return True

		return False






sol = Solution()
res = sol.hasCycle(head)
res2 = sol.hasCycleset(head)
res3 = sol.hasCyclepointer(head)

print(res)
print(res2)
print(res3)
