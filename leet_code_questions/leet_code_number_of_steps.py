"""
to calculate the nbumber of the steps 
either divide by zero or subtract 1 
"""

#test cases 

num1 = 14 
out1 =  6

num2 = 8
out2 = 4

class Solution:
    def numberOfSteps(self, num: int) :
    	"""
    	the number of steps to reduce the number
    	Args:
    		num(int) : the number to be reduced
    	Returns:
    		steps (int): the number of the steps
    	"""

    	steps = 0

    	#to solve the problem 

    	while num !=0:
    		if num % 2 == 0:
    			num = num/2
    			steps +=1
    		else:
    			num = num - 1
    			steps +=1

    	return steps



if __name__ == '__main__':
	soln = Solution()
	res = soln.numberOfSteps(num2)
	print(res)
