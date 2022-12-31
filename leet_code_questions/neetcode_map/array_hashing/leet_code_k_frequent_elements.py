"""
Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.
"""


nums = [1,1,1,2,2,3]
k = 2
out = [1,2]

nums2 = [1]
k2 = 1
out2 = 1

nums3 = [-1,-1]
k3 = 1

#complexity wanted is nlogn



#the brute force approach

class Solution:
    def topKFrequent(self, nums: list, k: int)-> list:
    	"""
    	The function takes the list of the integers and return the most frequnet elements
    	Args:
    		nums: (list) The list of the intgers 
    		k: (int) The number of the most frequent elements
		Return:
			frequency_lst: (list) the frquency of the most occured elements
    	"""
    	frequency_map = {}

    	for number in nums:
    		if number not in frequency_map:
    			frequency_map[number] = 0
    		count = frequency_map[number]
    		frequency_map[number] = count+1 

    	sorted_map = sorted(frequency_map.items(), key=lambda x:x[1], reverse=True)

    	print(sorted_map)
    	return sorted_map[0:k]


if __name__ == '__main__':
	sol = Solution()
	res = sol.topKFrequent(nums,k)
	print(res)

