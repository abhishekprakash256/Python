"""
Python make the queues
using the linked list implementation
methods are enque, deque, peek
"""


#problem with the dequeue method not popping out 

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

			temp = self.tail

			while True:
				if temp.next is None:
					self.head = temp
					break
				temp = temp.next
	
	def dequeue(self):
		temp = self.tail

		while True:
			if temp.next.next is None:
				temp = self.head
				temp.next = None 
				break
			temp = temp.next



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
my_queue.enqueue(5)
my_queue.enqueue(6)


print("The queue before : -------------")
print(my_queue.print_queue())

my_queue.dequeue()


#print the tail and the head
#print(my_queue.tail.data)
#print(my_queue.head.data)

#print the queue
print("The queue after deque : ------------------")
print(my_queue.print_queue())

