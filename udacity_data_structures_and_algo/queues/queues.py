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

		node = self.tail
		self.tail = node



