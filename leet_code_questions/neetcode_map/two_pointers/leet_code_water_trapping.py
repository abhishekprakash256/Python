"""
Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.

"""

height = [0,1,0,2,1,0,1,3,2,1,2,1]
out = 6 


class Solution:
    def trap(self,height)->int:
        """
        The function calculates the water trap in the ladder
        Args:
            height: (list) The list shows the height of the ladder 
        Returns:
            unit: (int) The water trapped in the units 
        """
        trap_water = False
        left = 0 
        right = left +1
        length = len(height) - 1 
        area_sum = 0

        while right <= length :
            
            if height[left] > 0 and height[left] > height[right]:
                trap_water = True

            elif trap_water == True and height[left] > height[right]:
                right +=1

            elif trap_water == True and height[left] < height[right]:
                trap_water = False
                area = min(height[left],height[right]) * (right - left)

                while left < right:
                    
                    area = area - height[left]
                    left+=1

                left = right
                right = right+1
                area_sum = area + area_sum

            elif height[left] == height[right]:
                trap_water = False
                left +=1
                right +=1
            
            print(right) 
           
            
        
        return area_sum


sol = Solution()
res = sol.trap(height)
print(res)  
               
        
             
