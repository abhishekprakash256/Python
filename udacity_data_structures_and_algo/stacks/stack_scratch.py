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
			node.next = self.head
			self.head = node

	def pop(self):
		temp = self.head

	def print_stack(self):
		temp = self.head
		
		print("The stack is -->")

		while True:
			print(temp.data)
			if temp.next is None:
				break
			temp = temp.next




#make the stack

my_stack = Stack()


#push the elements 
my_stack.push(1)
my_stack.push(2)
my_stack.push(3)
my_stack.push(4)
my_stack.push(5)


#pop the elements 

my_stack.pop()

#the pop function doesn't work 

my_stack.print_stack()