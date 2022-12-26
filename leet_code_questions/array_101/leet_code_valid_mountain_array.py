"""
The code for the valid mountain array problem
the array has to be strictly increasing or decreasing 
the array can be decreasing and increasing as well
example - 
[2,1,0,1,2]  #decreasing and increasing 
[3,4,5,6,3,1] #the increasing and increasing strictly

[1,2,3,4,4,5,2,1]  #not a valid mountain 

"""



"""
edge case 
length 1 or 2 return False 

incresing and equal value then False 

increase and decrease 

decrease or increase 

two way traverse 


"""
test0 = [1,2,3,2,1,0] #True ,passed

test1 = [3,2,1,2,3]  #True , passed

test2 = [3,3,2,1]  #False  , passed 
 
test3 = [0,1,2,1,0]  #True , passed

test4 = [1,2]  #False , passed
 
test5 = [1,2,3,4,2,2]  #False ,passed

test6 = [1,3,1]  #True , passed

test7 = [1,0,1]  #True , passed

test8 = [0,3,2,1]  #True ,  passed


class Solution:
	def validMountainArray(self,arr:list):
		"""
		The valid array mountain check for the up and down array 
		"""
		i = 0
		count = 0
		inc = False
		dec = False

		if len(arr) == 0 or len(arr) == 1 or len(arr) == 2:
			return False

		while (i < len(arr) - 1 ):

			if arr[i] == arr[i+1]:
				return False
				break

			elif arr[i] < arr[i+1] and inc == False and dec == False: 
				inc = True

			elif arr[i] > arr[i+1] and inc == False and dec == False:
				dec = True

			elif inc == True :
				
				if arr[i] > arr[i+1]:
					count+=1
					dec = True
					inc = False
				else:
					pass

			elif dec == True :

				if arr[i] < arr[i+1]:
					count +=1
					inc = True
					dec = False
				else:
					pass
			i+=1

		if count == 1:
			return True
		else:
			return False

if __name__ == '__main__':
	sol = Solution()
	res = sol.validMountainArray(test7)

	print(res)