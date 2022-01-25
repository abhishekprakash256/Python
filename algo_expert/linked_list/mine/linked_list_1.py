'''
implementaion of the doubly linked list using python
'''
class Node:
	def __init__(self,data):

		self.data = data
		self.next = None
		self.prev = None

class Doubly_linked_list:
	def __init__(self):
		self.head = None

		self.tail = None


	#the method to set the head and the following elements

	def append_element(self,data):

		new_node = Node(data) #the data has the node architecture

		#now we can set the head 

		if self.head is None:
			self.head = new_node #head is set 

		#when the head is not none 

		#we can use a loop iterator to iterrate every value till hit none

			return "head is set"

		
		else:

			#setting the temp varibale to the head 

			cur = self.head

			#iterative loop

			while cur.next is not None:
				
				#increasing the value 

				cur = cur.next

			#setting the next value to the new node

			cur.next = new_node

			#setting the prev value 

			new_node.prev = cur

			self.tail = new_node

			return "node is set"  


	#set the element in a index position 

	def insert_at_index(self, data, index):

		#make the new node

		new_node = Node(data)

		#Set the head to the cur node

		cur = self.head

		#set the pos variable 

		pos = 0

		#iterate the loop 

		while pos< index:

			#increase the pos
			pos +=1

			#increase the cur to next

			cur = cur.next

		#set the node at the index position 

		cur.prev.next = new_node

		new_node.prev = cur.prev

		cur.next.prev = new_node

		new_node.next = cur.next

		cur.next = None

		cur.prev = None

		return "The elememt is set at position: ",index



	#removal method of the given position 

	def search_node(self,node):

		#set the cur vale 

		cur = self.head 

		#set the node 

		new_node = Node(node)

		#iterate the node

		while cur.next is not None:

			#check the cur.data is found

			if cur.data == new_node.data:

				#check the return found 

				return "found the element"

			else:

				#increase the value 

				cur = cur.next

		#return if not found

		return "not found the element"


	def print_list(self):

		#temp variable will store the head

		cur = self.head

		#loop iteration 

		while cur.next is not None:

			print(cur.data) #printing of the data 

			cur = cur.next #next iteration


		print(cur.data)

		return "printed list"


	#remove the head 

	def remove_head(self):

		#set the head

		cur = self.head

		#the second elemnet 

		cur = cur.next

		#setting to none 
		cur.prev = None

		#set the head next to none

		self.head.next = None

		self.head = cur #set the head

		return "Head is removed"

	def remove_tail(self):

		#set the cur variable 

		cur = self.tail

		# set to previous elememnt

		cur = cur.prev

		#remove process

		cur.next = None  #Set to none

		self.tail.prev = None  #set to none

		self.tail = cur #tail is set

		return "Tail is removed"


	def remove_index(self, index):

		# position varibale 
		
		pos = 0

		#this for iteration

		cur = self.head

		#loop is started

		while pos < index :

			pos +=1  #position is increased

			cur = cur.next #cur is itertated 

		#removal part

		print("this is removed" , cur.data)

		cur.next.prev = cur.prev

		cur.prev.next = cur.next

		return "Removal is done"






#make the instance

my_list = Doubly_linked_list()

print(my_list.append_element(4))

print(my_list.append_element(2))

print(my_list.append_element(1))

print(my_list.append_element(6))

print(my_list.append_element(1))

print(my_list.append_element(7))

print(my_list.append_element(9))

print(my_list.append_element(2))

print(my_list.append_element(3))

print(my_list.append_element(5))

print(my_list.print_list())


print(my_list.search_node(0))



print(my_list.remove_head())


print(my_list.print_list())


print(my_list.remove_tail())


print(my_list.print_list())

print(my_list.remove_index(2))

print(my_list.print_list())


print(my_list.insert_at_index(12, 3))

print(my_list.print_list())