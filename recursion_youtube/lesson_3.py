"""
The program to find the linked list of the 
"""

class Node():
	def __init__(self,data):
		self.data = data
		self.next = None


#my list -------------------------------------------------------------
node0 = Node(4)
node1 = Node(5)
node2 = Node(6)
node3 = Node(7)
node4 = Node(8)

node0.next = node1
node1.next = node2
node2.next = node3
node3.next = node4


#---------------------------------------print the list------------
print(node0.data)
print(node0.next.data)
print(node0.next.next.data)
print(node0.next.next.next.data)
print(node0.next.next.next.next.data)
#---------------------------------------------


def reverse_list(temp):
	"""
	The function takes the node of the linked list and reverse the list
	Args:
		temp: (root node of list) The node of the linked list
	Return:
		revered_list: (the list is reversed) The reveresed list of the linked list 
	"""
	if temp.next is None :
		return temp.data
	else:
		return 
