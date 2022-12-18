"""
Merge the sorted array the first in the second one 
num1 is the bigger array 
num2 is the smaller array 
both are the sorted array 
m the number of the sorted elements in the num1
n the number of the sorted elements in the num2
"""


class Solution:
	def merge(self,list1,m,list2,n):

		i = 0
		j = 0 

		while 