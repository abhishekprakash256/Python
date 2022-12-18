"""
Delelte the elements from the givnen array and return the rest array 
modify the given array not make a copy

"""
lst = [1,2,3,2,5,6]
val = 2
out = [1,3,5,6]


lst2 = [3,3]
val2 = 3
out2 = [] 


lst3 = [1,1]
val3 = 1
out3 = []


class Solution:
	def removeElement(self,lst,val):
		"""
		The elements of the array are taken and removed
		the modified array is give out 
		Args:
			lst : (list) The array of the elements 
			val : (int) The element that need to be removed

		"""
		self.lst = lst
		self.val = val
		for i in range(len(self.lst)):
			if self.val not in self.lst:
				break
			self.lst.remove(self.val)

if __name__ == '__main__':
	sol = Solution()
	print(lst3)
	res = sol.removeElements(lst3,val3)
	print(lst3)
