#the optimal solions
'''
Given a string s, find the length of the longest substring without repeating characters.

 

Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.

Example 2:

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.

Example 3:

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.

Example 4:

Input: s = ""
Output: 0

'''

# the trick is to use a set to update the elements and pop them and chek if the strings are present or not 
# work in the sliding window algorithm

# code 

inp = input("Enter the string: - ")

class Solution:
	def lengthOfLongestSubstring(self,s:str) -> int:
		#making a set 
		char_set = set()
		l = 0  # to maintain the length of the checked number
		res = 0  # make the result
		for r in range(len(s)):
			#while loop will work in the char set to pop out the elements
			while s[r] in char_set:
				char_set.remove(s[l])
				l+=1
			char_set.add(s[r])
			res  = max(res, r - l + 1)
		return res


test = Solution()

print(test.lengthOfLongestSubstring(inp))