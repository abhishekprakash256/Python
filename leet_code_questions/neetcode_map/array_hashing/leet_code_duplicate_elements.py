"""
Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

"""


nums0 = [1,2,3,1] #True

nums1 = [1] # False

nums2 = [1,2,3,4]  #False

"""
idea will be 
keep a counter var 
set to 0
has a hash map set to empty 
see the value in put in hash map 
if matches count set to +1
return 0 if count == 0 else return 1

"""


class Solution:
    def containsDuplicate(self, nums: list) -> bool:
    	"""
    	The function checks the value in the integer and if repeats return True or False
    	Args:
    		nums : (list) The array of the list that has integers
    	Return:
    		True or False : (bool) if the value exists or not 
    	"""
    	if len(nums) == 0 or len(nums) == 1:
    		return False

    	count = 0 
    	map_val = {}

    	for i in nums:
    		if i not in map_val:
    			map_val.update({i:True})
    		else:
    			return True

    	return False

if __name__ == '__main__':
	sol = Solution()
	res = sol.containsDuplicate(nums0)
	print(res)
