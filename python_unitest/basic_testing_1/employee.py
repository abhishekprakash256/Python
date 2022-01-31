"""
The class for the employee 
"""

class Employee:
	def __init__(self,first,last,pay):
		self.first = first 
		self.last = last
		self.pay = pay


	@property
	def full_name(self):
		return '{},{}'.format(self.first,self.last)

	@property
	def email(self):
		return '{}{}@email.com'.format(self.first,self.last)


	def raise_pay(self,value):
		self.value = value
		return self.pay + value

