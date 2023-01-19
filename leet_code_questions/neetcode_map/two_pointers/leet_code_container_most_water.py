"""
You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container, such that the container contains the most water.

Return the maximum amount of water a container can store.

Notice that you may not slant the container.


"""

height = [1,8,6,2,5,4,8,3,7]
out = 49 




#brute force solution

class Solution:
    def maxArea_brute_force(self,lst:list)->int:
        """
        The function calculates the max area between the given bars
        Args:
            lst: (list) the area of the bars
        Return
            max_area: (int) the max area in the  
        """
        max_area = 0
        
        for i in range(0,len(lst)):
            
            for j in range(i+1,len(lst)):
                
                #area calculation
                temp_area = min(lst[i],lst[j])*(j-i)
            max_area = max(temp_area,max_area)
        return max_area

    def maxArea(self,nums:list)->int:
        """
        The function calculates the max area between the given bars
        using the twop pointer approach
        Args:
            lst: (list) the area of the bars
        Return
            max_area: (int) the max area in the 
        
        """
        left = 0
        right = len(nums) - 1
        max_area = 0

        while left < right:
            area = min(nums[left],nums[right]) * (right - left)
            max_area = max(area,max_area)

            if nums[left] > nums[right]:
                right -=1
            elif nums[left] < nums[right]:
                left +=1
            else:
                right -=1
                left +=1
       
        return max_area
            


          

sol = Solution()
res = sol.maxArea(height)
print(res)        
