"""
The mountan is like a zig zag 
not equal points only increasing or decrasing 
"""

test0 = [1,2,3,2,1,0] #True ,passed

test1 = [3,2,1,2,3]  #False , passed

test2 = [3,3,2,1]  #False  , passed 
 
test3 = [0,1,2,1,0]  #True , passed

test4 = [1,2]  #False , passed
 
test5 = [1,2,3,4,2,2]  #False ,passed

test6 = [1,3,1]  #True , passed

test7 = [1,0,1]  #False , passed

test8 = [0,3,2,1]  #True ,  passed

test9 = [0,1,2,1,2]  #True, 

test10 = [0,1,2,3,4,5,6,7,8,9]  #False


class Solution:
	def validMountainArray(self,arr:list):
		"""
		The valid array mountain check for the up and down array 
		"""
		i = 0
		count = 0 
		inc = False

		if len(arr) == 0 or len(arr) == 1 or len(arr) == 2:
			return False

		while (i < len(arr) - 1 ):

			if i == 0 and arr[i] > arr[i+1]:
				return False
			elif arr[i] == arr[i+1]:
				return False
			elif arr[i] < arr[i+1] and inc == False:
				inc = True
			elif inc == True:
				if arr[i] > arr[i+1]:
					count+=1
					inc = False
			i+=1

		if count >=1:
			return True
		else:
			return False

if __name__ == '__main__':
	sol = Solution()
	res = sol.validMountainArray(test9)
	print(res)