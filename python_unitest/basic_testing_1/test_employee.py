"""
The file is used for making the test cases for the Employee class
"""

import unittest

from employee import Employee


#make the test class

class Test_Employee(unittest.TestCase):
	"""
	The class to test the employee
	"""
	
	#testing the name 

	emply_0 = Employee('Abhi', 'Prakash', 500)
	emply_1 = Employee('Tom', 'Jerry', 500 )

	def test_name(self):


		self.assertEqual(self.emply_0.first ,'Abhi')
		self.assertEqual(self.emply_1.last,'Jerry')

	#testing the email

	def test_email(self):

		self.assertEqual(self.emply_0.email, 'AbhiPrakash@email.com')
		self.assertEqual(self.emply_1.email, 'TomJerry@email.com')

	#test the pay raise 

	def test_pay_raise(self):

		self.assertEqual(self.emply_0.raise_pay(400), 900)
		self.assertEqual(self.emply_1.raise_pay(300), 800)


if __name__ == '__main__':
	unittest.main()