"""
Given an array of integers temperatures represents the daily temperatures, return an array answer such that answer[i]
is the number of days you have to wait after the ith day to get a warmer temperature. 
If there is no future day for which this is possible, keep answer[i] == 0 instead
"""

#test cases
temp0 = [73,74,75,71,69,72,76,73]
out0 = [1,1,4,2,1,1,0,0]


temp2 = [30,40,50,60]
out2 = [1,1,1,0]  

temp3 = [30,60,90]
out3 = [1,1,0]



class Solution:
    def dailyTemperatures(self, tempr_lst: list):
        """
        The function calculates the max tempr for the next ith day
        Args:
            tempr: (int) The list of the tempr
        Return:
            max_list: (int) The list of the tempr that are higher than the day
        """
        res = [0]*len(tempr_lst)
        stack = []

        for i,t in enumerate(tempr_lst):

            while stack and t > stack[-1][0]:
                stackT,stackInd = stack.pop()
                res[stackInd] = (i - stackInd)
            stack.append([t,i])
                

        return res


sol = Solution()
res = sol.dailyTemperatures(temp0)
print(res)
                
            
            

             
        
        
