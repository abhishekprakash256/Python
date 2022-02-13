"""
The python code for the sphinx

"""

import pytest
import pymongo
import os


def add(a:int, b:int)->int:
	"""
	The function returns the value of two integers

	Arguments:
		a: (int) the value of integer
		b: (int) the value of integer

	Returns:

		sum (int) the sum of two numbers

	"""
	sum = a+b
	
	return sum

'''
class Person:
	"""
	The class to hold the data of the person
	Attribute: (name), (age) , (unique_id)


	"""
	def __init__(self,name,age,unque_id):
		self.name = name
		self.age = age
		self.unque_id = unque_id 

	def change_name(self,new_name):
		"""
		The method assigns a new name to the person
		Attributes: new_name (str)

		"""
		self.name = new_name

	def change_age(self,new_age):
		"""
		The method assigns a new age to the person
		Attributes: new_age (int)
		"""
		self.age = new_age

	def change_unique_id(self,new_id):

		"""
		The method assigns a new id to the person
		Attributes: new_id (int)
		"""
		self.unque_id = new_id'''


if __name__ == "__main__":

	print(add(3,3))
	
	"""abhi = Person("Abhi", 25, 1)
	abhi.change_name("Abhishek")"""
