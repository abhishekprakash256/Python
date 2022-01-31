"""
the unit test file 
"""

import unittest

import calc


#make the class 
class TestCalc(unittest.TestCase):

	#make the test method
	def test_add(self):
		#result = calc.add(3,5)
		self.assertEqual(calc.add(3,5),8)
		self.assertEqual(calc.add(3,2),5)
		self.assertEqual(calc.add(3,1),4)
		self.assertEqual(calc.add(3,-1),2)

	#anothe method for the testing
	def test_sub(self):
		#result = calc.add(3,5)
		self.assertEqual(calc.sub(3,1),2)
		self.assertEqual(calc.sub(3,2),1)
		self.assertEqual(calc.sub(3,-1),4)
		self.assertEqual(calc.sub(3,0),3)
	

	def test_mul(self):
		#result = calc.add(3,5)
		self.assertEqual(calc.mul(3,1),3)
		self.assertEqual(calc.mul(3,2),6)
		self.assertEqual(calc.mul(3,-1),-3)
		self.assertEqual(calc.mul(3,0),0)

	def test_divide(self):
		#result = calc.add(3,5)
		self.assertEqual(calc.divide(3,1),3)
		self.assertEqual(calc.divide(3,2),1.5)
		self.assertEqual(calc.divide(3,-1),-3)
		self.assertEqual(calc.divide(3,3),1)
		#value error test case
		self.assertRaises(ValueError, calc.divide, 3,0)

		#by using the context manager

		with self.assertRaises(ValueError):
			calc.divide(4,0)
	

	def test_remain(self):
		#result = calc.add(3,5)
		self.assertEqual(calc.remain(3,1),0)
		self.assertEqual(calc.remain(3,2),1)
		self.assertEqual(calc.remain(3,-1),0)






#make the main method
if __name__ == '__main__':
	unittest.main()
