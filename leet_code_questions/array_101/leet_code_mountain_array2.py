"""
Check the array is the mountain or not
the array has to increase linearly and decrsase linearly 

"""
arr = [2,1]
out = False

arr2 = [3,5,5]
out2 = False

arr3 = [0,3,2,1]
out3 = True



class Solution:
	def validMountainArray(self,arr:list):
		"""
		The function checks the array is a mountain array or not
		Args:
			arr : (list) The array of the integers
		Return:
			True or False : (bool) The array is mountain or not 
		"""

		if len(arr) < 3:
			return False

		i = 0
		j = 1
		condn = True
		count = 0

		while (i < len(arr) -1):
			if condn == True:
				if arr[i] < arr[j]:
					condn = True
				elif arr[i] == arr[j]:
					return False
				else:
					condn = False
					count +=1
				i+=1
				j+=1
			else:
				if arr[i] > arr[j]:
					condn = False
				elif arr[i] == arr[j]:
					return False

				i+=1
				j+=1

		if count == 1:
			return True
		else:
			return False

if __name__ == '__main__':
	sol = Solution()
	res = sol.validMountainArray(arr3)
	print(res)