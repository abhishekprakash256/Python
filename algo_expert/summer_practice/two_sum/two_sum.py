"""
The qusestion is two find the sum to two numbers that are equal to a given number 
numbers can be -ve and postive and zero

input - lst of integers
output - two integers
"""

#test cases
lst1 = [1,2,3,4,6,7,8]  #7
target1 = 7
out1 = [1,6]

lst2 = []
target2 = 3
out2 = None

lst3 = [1,3,4,6,7,3,5,8]
target3 = 100
out3 = None    

lst4 = [1,1,1,1,1,1]
target4 = 2
out4 = [1,1]

lst5 = [1,1,1,1,4,5]
target5 = 9
out5 = [4,5]



testing_lst = [[lst1,target1,out1],[lst2,target2,out2],[lst3,target3,out3],[lst4,target4,out4],[lst5,target5,out5]]



#the brute force approach
def two_sum_brute(array: list , target: int)-> list:
	"""
	The function takes a list of integers and gives  two numbers that's sum is equal to the target
	Args: 
		array (list): the list of integers
		target (int): the target sum
	Returns:
		val_lst (list): the list of two integers  

	"""
	array_len = len(array) #the len of the array 
	ans_lst = []
	

	for i in range(0,array_len-1): #first loop 
		for j in range(1,array_len): #second loop
			
			if array[i]+ array[j] == target : #checking
				 
				ans_lst.append(array[i])  # appendind the values
				
				ans_lst.append(array[j])
				
				return ans_lst #return the list 
			
			else:
				
				continue 


	return None #return if not found any



#the sorting list approach 

def two_sum_sort(array:list, target:int)-> list:
	"""
	The function takes a list of integers and gives  two numbers that's sum is equal to the target
	Args: 
		array (list): the list of integers
		target (int): the target sum
	Returns:
		val_lst (list): the list of two integers  

	"""
	res_lst = [] #the elements in the result 

	array.sort()

	left_ptr = 0 #left pointer 
	right_ptr = len(array)- 1 #right pointer

	while left_ptr < right_ptr:
		if array[left_ptr] + array[right_ptr] == target: #check for the sum
			res_lst.append(array[left_ptr])  #append the value
			res_lst.append(array[right_ptr])
			return res_lst  #return value 

		elif array[left_ptr] + array[right_ptr] < target: #left decrease
			left_ptr +=1	

		elif array[left_ptr] + array[right_ptr] > target: #right increase
			right_ptr -=1

	return None  #return None if not found



#the hash list approach

#the fastest approach to find the soln

def two_sum_hash(array:list, target:int)-> list:
	"""
	The function takes a list of integers and gives  two numbers that's sum is equal to the target
	Args: 
		array (list): the list of integers
		target (int): the target sum
	Returns:
		val_lst (list): the list of two integers  

	"""
	found_element = {} #empty dict
	res_lst = []

	for i in array:
		diff = target - i
		
		if diff in found_element:
			res_lst.append(diff)
			res_lst.append(i)
			return res_lst 
		
		found_element[i] = True

	return None




print(two_sum_hash(lst5,target5))



#added the unitesting of the 

import unittest

class test_method(unittest.TestCase):

	def test_fun1(self):
		for i in testing_lst:	
			self.assertEqual(two_sum_brute(i[0],i[1]), i[2])
	
	def test_fun2(self):
		for i in testing_lst:
			self.assertEqual(two_sum_sort(i[0],i[1]),i[2])
	def test_fun3(self):
		for i in testing_lst:
			self.assertEqual(two_sum_hash(i[0],i[1]),i[2])



if __name__ == '__main__':
	unittest.main()