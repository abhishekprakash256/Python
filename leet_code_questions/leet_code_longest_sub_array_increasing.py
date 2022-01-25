'''
The find that array that are increasing in the sub array always
'''

lst_1 = [0,1,2,4,3]  #3

lst_2 = [0,1,0,3,2,3]  #4

lst_3 = [0,3,1,6,2,2,7,7,7,7]  #4

lst_4 = [1,1]

lst_5 = [1]

lst_6 = [0,2,3]

lst_7 = [1,1,1,1,1]

class Solution:
	def __init__(self,lst):
		self.lst = lst
	def sub_array(self):
		lst = self.lst 
		lst.sort()
		length = 1
		if len(lst) == 1:
				length =1
		else:
			for i in range(len(lst)):
				if i == len(lst)-2:
					if lst[i]< lst[i+1]:
						length+=2
						break
					else:
						length = length
						break
				elif lst[i] < lst[i+1]:
					length+=1
				else:
					pass
		return length
			



check_1 = Solution(lst_3)

print(check_1.sub_array())
