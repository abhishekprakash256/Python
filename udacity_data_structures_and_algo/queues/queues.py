"""
Python make the queues
using the linked list implementation
methods are enque, deque, peek
"""

class Node:
	def __init__(self,data):
		self.data = data
		self.next = None


class Queue:
	def __init__(self):
		self.head = None
		self.tail = None

	def enqueue(self,data):
		node = Node(data)

		if self.tail is None:
			self.tail = node
		else:
			node.next = self.tail
			self.tail = node

			temp = self.head

			while True:
				if temp.next is None:
					self.tail = temp
					break
				temp = temp.next
	
	def dequeue(self,data):
		pass


	def print_queue(self):

		temp =self.tail
		while True:
			print(temp.data)
			if temp.next is None:
				break
			temp = temp.next


#initilaize the queue
my_queue = Queue()

#enqueue the elements in the queue
my_queue.enqueue(2)
my_queue.enqueue(3)
my_queue.enqueue(4)


print(my_queue.print_queue())