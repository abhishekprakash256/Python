"""
the most consecutive ones in the array

"""


#test cases for the array 

Input = [1,1,0,1,1,1]
Output =3


Input2 = [1,0,1,1,0,1]
Output2=  2 



class Solution:
    def findMaxConsecutiveOnes(self, nums: list) -> int:
        """
        The function gives the max number of the ones that are consecutive 
		Args :
			nums (list) : the array of the ones and zeros
		Returns:
			max (int) : the number of the max ones 
        """

        
        gobal_max= 0 
        temp_max = 0
        for i in nums:
        	if i == 1:
        		temp_max +=1
        	else:
        		temp_max=0

        	if temp_max > gobal_max:
        		gobal_max = temp_max

       	return gobal_max


if __name__ == '__main__':
	Soln = Solution()
	res = Soln.findMaxConsecutiveOnes(Input2)
	print(res)