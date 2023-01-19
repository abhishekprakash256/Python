"""
The leet code three sum problem to find the triplets of the zero 
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0

"""


#test cases 

inp = [-1,0,1,2,-1,-4]
out = [[-1,-1,2],[-1,0,1]]


inp2 = [0,1,1]
out2 = []


#the solution 


class Solution:
    def threeSum(self, nums):
        
        lst_sum = []
        left = 0 
        right = len(nums) - 1
        nums.sort()
        print(nums)
        
        for i in range(0,len(nums)):
            left = i+1
            while left<=right:
                if nums[left] + nums[right] + nums[i] == 0:
                    lst_sum.append(left)
                    lst_sum.append(right)
                    lst_sum.append(i)

                elif nums[left] + nums[right] + nums[i] > 0:
                    right -=1
                
                elif nums[left] + nums[right] + nums[i] < 0:
                     left +=1


        return lst_num



sol = Solution()
res = sol.threeSum(inp)
print(res)
                    
                    



 
