"""
The code for making a montonic stack decreasing order
"""

temp0 = [73,74,75,71,69,72,76,73]


class Solution:
    def dailyTemperatures(self, tempr_lst: list):
        """
        The function calculates the max tempr for the next ith day
        Args:
            tempr: (int) The list of the tempr
        Return:
            max_list: (int) The list of the tempr that are higher than the day
        """
        stack = []
        left = 0
        length = len(tempr_lst)  
    
        while left< length:
            
            if len(stack) == 0:
                stack.append(tempr_lst[left])
            
            elif stack[len(stack)-1] >= tempr_lst[left]:
                stack.append(tempr_lst[left])
            
            else:
                while True:

                    if len(stack) == 0 :
                        stack.append(tempr_lst[left])
                        break
                    
                    elif stack[len(stack)-1] < tempr_lst[left]:
                        stack.pop()

                    else:
                        stack.append(tempr_lst[left])
                        break                    
                   
            left+=1

        return stack

