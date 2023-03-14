"""
You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists in a one sorted list. The list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list.

"""


# Definition for singly-linked list.
class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next


#make the two linked list

node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)

node11 = ListNode(2)
node12 = ListNode(2)
node13 = ListNode(4)



#make the linked list 

node1.next = node2
node2.next = node3

node11.next = node12
node12.next = node13



#print the list 

def listPrint(node):
	temp = node
	while True:
		print(temp.val)
		if temp.next == None:
			break

		temp = temp.next




class Solution:
	def mergeTwoLists(self,node1,node2):

		i = node1
		j = node2

		if i.val >= j.val:
			start = j
		else:
			start = i 

		while True:

			nxti = i.next 
			nxtj = j.next

			if i.next == None and j.next == None :
				break

			elif i.val <= j.val :
				i.next = j

			else:
				j.next = i

			i = nxti
			j = nxtj 


		return start.val


sol = Solution()
res = sol.mergeTwoLists(node1,node11)

print(res)


