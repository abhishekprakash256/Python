"""
implementation of stack from the scratch using the linked list

"""

class Node:
	def __init__(self,data):
		self.data = data
		self.next = None

class Stack:
	def __init__(self):
		self.head = None

	def push(self,data):
		node = Node(data)

		if self.head is None:
			self.head = node
		else:
			node.next = self.head.next
			self.head = node


	def print_stack(self):
		temp = self.head
		
		while True:
			if temp.next is None:
				break
			print(temp.data)
			temp = temp.next


#make the stack

my_stack = Stack()

my_stack.push(2)
my_stack.push(3)
my_stack.push(4)

my_stack.print_stack()