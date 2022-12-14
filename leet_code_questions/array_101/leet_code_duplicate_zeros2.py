"""
The program to duplicate the zeros oin the array
"""

lst = [1,0,2,3,0,4,5,0]
out = [1,0,0,2,3,0,0,4]

lst2 = [1,2,3]
out2 =  [1,2,3]

lst3 = [0]
out3 = [0]



class Solution:
	def duplicateZeros(self, arr:list):
		"""
		The function to return the modified array as per question      
		Args:
			arr: (list) The input list
		Returns:
			arr: (list) The modified list
		"""
		length_arr = len(arr)
		i = 0
		while i< length_arr:
			if arr[i] == 0:
				arr.insert(i+1,0)
				i+=2
			else:
				i+=1 

		return arr[0:length_arr]


if __name__ == '__main__':
	sol = Solution()
	res = sol.duplicateZeros(lst)
	print(res)