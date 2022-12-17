"""
The implementation of the linked list from scratch

The methods are to print the list 
add the elements on head
at tail 
at any position
find the element and delete it 



"""
#A dummy elementnetataion of the node and adding the node manually
class Node:
	def __init__(self,data):
		self.data = data
		self.next = None

"""
#add the nodes		
head = Node(2)
second_node = Node(3)
tail_node = Node(4)


#connect the nodes 
head.next = second_node
second_node.next = tail_node
tail_node.next = None

"""

class Linked_list:
	def __init__(self):
		self.head = None

	def set_head(self,data):
		if self.head is None:
			node = Node(data)
			self.head = node
		else:
			node = Node(data)
			node.next = self.head
			self.head = node 

	def print_list(self):
		temp = self.head
		
		while True:
			print(temp.data,"->" , end = " ")
			if temp.next is None:
				break
			temp = temp.next


	def get_length(self):
		count = 1
		temp = self.head 

		while True:
			count+=1
			if temp.next is not None:
				temp = temp.next
			else:
				break

		return  f'The length is {count}'


	def add_node(self,pos,data):
		self.pos = pos
		node = Node(data)
		count = 1 
		temp = self.head

		while True:
			if count < self.pos:
				count +=1
			else:
				node.next = temp.next
				temp.next = node
				break

			temp = temp.next
			

	def delete_node(self,data):
		node = Node(data)
		temp = self.head
		self.data = data

		while True:
			if temp.next.data == self.data:
				temp.next = temp.next.next
				break
			temp = temp.next



my_list = Linked_list()

my_list.set_head(2)

my_list.set_head(3)

my_list.add_node(1,4)

my_list.add_node(2,8)

my_list.add_node(3,5)

my_list.set_head(10)

my_list.delete_node(5)

print(my_list.print_list())
print(my_list.get_length())