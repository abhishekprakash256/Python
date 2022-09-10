"""
The question is to find the middle of the linked list
"""

#test cases


Input1 = [1,2,3,4,5]
Output1 = [3,4,5]


#Definition for singly-linked list.
class ListNode:
	def __init__(self, val=0, next=None):
         self.val = val
         self.next = next




class Solution:
    def middleNode(self, head):
    	"""
    	The function returns the middle of the linked list 
		Args:
			head (node) : the head node of the linked list
		Returns:
			middle_node_val (node): the middle node of the linked list or the second node 
    	"""

    	temp = head
    	
    	count =0

    	#get the length of the linked list 
    	while True:
    		if temp.next  == None:
    			count+=1
    			break

    		count+=1
    		temp = temp.next

    	#the check of the length
    	if count %2 == 0:
    		index = (count/2)+1
    	else:
    		index = (count+1)/2

    	pointer = 0
    	temp1 = head
    	while pointer < index -1:
    		temp1 = temp1.next
    		pointer +=1
    		

    	return temp1

if __name__ == '__main__':
	#to make the linked list
	node1 = ListNode(1)
	node2 = ListNode(2)
	node3 = ListNode(3)
	node4 = ListNode(4)
	node5 = ListNode(5)

	node1.next = node2
	node2.next = node3
	node3.next = node4
	node4.next = node5

	Soln = Solution()
	res = Soln.middleNode(node1)
	print(res)