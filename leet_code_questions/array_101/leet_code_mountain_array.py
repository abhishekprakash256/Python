"""
The question for finding the mountain array 
The values have to be constantly increasing and then decreasing

1<2<3<4<5>4>3>2>1
"""

arr = [2,1]
out = False

arr2 = [3,5,5]
out2 = False

arr3 = [0,3,2,1]
out3 = True


"""
explanantion 

first edge case 
if length is less than 3

[1,2,3] #not tree

[1,1,,2,3,2] #not mountain tree

[1,2,3,4,2,1]  #this is mountain 

"""

#varun implementation of the code ------------------------------------------------------

class Solution:
	def validMountainArray(self, arr: list) -> bool:
		"""
		The function checks the array is the mountain or not
		Args :
			arr : (list) The list of the integers to check the mountain array 
		Return :
			True or False : (Bool) The array is mountain or not
		"""
		i = 0
		condn = True

		while(i < len(arr) -1):

			if (arr[i] > arr[i+1]):
				condn = False
				i+=1
				break
			i+=1
		if(i==len(arr)-1):return False
		while( i < len(arr) -1 ):
			if (arr[i] <= arr[i+1]):
				return False
			i+=1

		return True

if __name__ == '__main__':
	soln = Solution()
	res = soln.validMountainArray(arr3)
	print(res)
