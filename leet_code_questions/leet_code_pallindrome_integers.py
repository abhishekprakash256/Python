"""
The program is to find the pallindroim integers 

"""

#test cases 

inp = 121
out = True

inp2 = -121
out2 = False


inp3 = 10 
out3 = False


inp4 = 1
out4 =  True



class Solution:
    def isPalindrome(self, x: int) -> bool:
    	"""
    	The function to check the integers are pallindrome are not 

    	Args:
    		x (int) : the integer 
    	Returns:
    		True or False (Bool) : the boolean value true or false to check the pallindrome

    	"""
    	x = str(x)
    	left = 0
    	right = len(x) - 1

    	while left <=right:
    		if x[left] == x[right]:
    			left +=1
    			right -=1
    		else:
    			return False
    	
    	return True

if __name__ == '__main__':
	Soln = Solution()
	res = Soln.isPalindrome(inp)
	print(res)