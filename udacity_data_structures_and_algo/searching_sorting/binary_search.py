"""
Implement the binary search from scratch 
in a list
"""

"""
take the divide it array 
take the middle element and compare it and if can't be divided then peek the left and right 
based on that go to the left array or the right array
repeat it again till the element found 
if not found return False
"""

class Searching:
	def binary_search(self,arr,val):
		"""
		The fucntion takes the value of the array and the searching val 
		and search the val in the array
		Args:
			arr : (list) The integer of the array 
			val : (int) the value of the integer to search 
		Return:
			True or False: (bool) The element found or not 
		"""

		