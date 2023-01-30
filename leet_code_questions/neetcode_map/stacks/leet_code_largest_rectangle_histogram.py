"""
Given an array of integers heights representing the histogram's bar height where the width of each bar is 1, 

return the area of the largest rectangle in the histogram.
"""

height0 = [2,1,5,6,2,3]
out0 = 10 

height1 = [2,4]
out1 = 4 


class Solution:
    def largestRectangleArea(self, heights:list) -> int:
        """
        The function takes the array of the heights and calculate the max height
        Args:
            heights: (list) The array of the heights
        Return:
            max_area: (int) The max area of the rectangle can be made
        """

        data_stack = []
        max_area = 0 

        for i,h in enumerate(heights):
            
            if len(data_stack) == 0 :
                data_stack.append([i,h])
            
            if data_stack[len(data_stack)-1][1] < h:
                temp_ele = data_stack.pop()
                max_area = max(temp_ele * (i))
            
            else:
                data_stack.append([i,h])
                
                for a in reversed(data_stack):
                   area = a[1]*(a[0])
                   max_area = max(area,max_area)       
                    
        return max_area
                        


sol = Solution()
res = sol.largestRectangleArea(height0)        

print(res)
