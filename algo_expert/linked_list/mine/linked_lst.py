'''
Linked list implementation, with the helper methods 
'''

class DoublyLinkedList():
	def __init__(self):
		self.head = None
		self.tail = None
		self.prev = None
		self.next = None

	#make the set head method

	def sethead(self,node):

		self.node = node

		if self.head == None:
			self.node = self.head
		else:
			self.head.prev = self.node
			self.node.next = self.head
			self.node.prev = None

		return node

	def settail(self,node):

		self.node = node
		
		if self.tail == None:
			self.node = self.tail
		else:
			self.tail.prev = self.node
			self.node.next = self.tail
			self.node.prev = None

		return node

	def search_node(self,node):

		self.node = node
		#self.head = self.node    #set the head node
		#self.node = node
		#self.prev = None
		#self.next = None
		#self.node.prev = None
		#self.node.next = None

		while self.node.next is not self.node : #start for the loop
			
			self.temp =  None  #set the temp variable

			self.node.next = self.temp

			self.temp.next = self.node.next

			return True

		return False


lst = DoublyLinkedList()

print(lst.sethead(2)) 
print(lst.settail(3))
print(lst.settail(6))

print(lst.search_node(4))