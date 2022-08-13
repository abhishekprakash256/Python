"""
to iterate over a list and store in the lined list

"""
l1 = [1,2,3,4]


class node():
	def __init__(self,next=None, val =0):
		self.next = next
		self.val = val


class linked_list():
	def __init__(self):
		self.head = None

	def make_lst(self,lst):

		#iterate over the list 
		i= 0 
		while i < len(lst):
			

			if self.head is None:
				curr = node()
				self.head = curr
				self.head.val = lst[i]

			else:
				#curr = node()
				curr.val = lst[i]
			
			node2 = node()
			curr.next = node2

			print(curr.val)
			
			print(lst[i])
			i+=1
		print(self.head.val)

	






if __name__ == '__main__':
	test_lst = linked_list()
	print(test_lst.make_lst(l1))