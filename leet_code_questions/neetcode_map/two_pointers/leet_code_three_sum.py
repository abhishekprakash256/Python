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
        
        lst_num = []
        nums.sort()
        print(nums)
        
        for i in range(0,len(nums)):
            
            if i > 0 and nums[i] == nums[i-1]:
                continue

            
            left = i+1
            right = len(nums) - 1

            while left < right:
                temp_lst = []
                
                if nums[left] + nums[right] + nums[i] == 0:
                    
                    if nums[left] != nums[right] != nums[i]:                    
                        temp_lst.append(nums[left])
                        temp_lst.append(nums[right])
                        temp_lst.append(nums[i])

                        left +=1
                        while nums[left] == nums[left-1] and left < right:
                            left +=1
                    

                elif nums[left] + nums[right] + nums[i] > 0:
                    right -=1
                
                elif nums[left] + nums[right] + nums[i] < 0:
                     left +=1
                
                if len(temp_lst) > 1:
                    lst_num.append(temp_lst)


        return lst_num



sol = Solution()
res = sol.threeSum(inp)
print(res)
                    
                    



 
