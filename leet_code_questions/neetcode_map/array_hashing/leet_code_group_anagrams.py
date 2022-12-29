"""

Given an array of strings strs, group the anagrams together. You can return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

"""

#test cases 

strs0 = ["eat","tea","tan","ate","nat","bat"]
output0 = [["bat"],["nat","tan"],["ate","eat","tea"]]

strs1 = [""]
output1 = [[""]]

strs2 = ["a"]
output2 =[["a"]]

#sorted_word = ''.join(sorted(strs[i]))


#-------------the solution works but the time limit exceeds ------------------------

class Solution:
    def groupAnagrams(self, strs: list) -> list:
    	"""
    	To check the anagram from the group of the list and arranage in the list together
    	Args:
    		strs: (list) The list of the anagram 
    	Return:
    		arrange_lst: (list) The list of the arranged anagram together in sub list
    	"""
    	arranged_lst = []
    	i = 0
    	while len(strs) !=0:
    		
    		word_visited = []
    		first_word = ''.join(sorted(strs[0]))
    		word_visited.append(strs[0])
    		strs.remove(strs[0])

    		for j in range(0,len(strs)):
    			second_word = ''.join(sorted(strs[j]))
    			if first_word == second_word:
    				word_visited.append(strs[j])

    		arranged_lst.append(word_visited)
    		for k in range(1,len(word_visited)):
    			strs.remove(word_visited[k])
    	
    	return arranged_lst 
    		
if __name__ == '__main__':
	sol = Solution()
	res = sol.groupAnagrams(strs1)
	print(res)