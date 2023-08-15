"""
Given a string s, find the length of the longest
substring
without repeating characters.

"""

#test case 

s0 = "abcabcbb"
out0 = 3 

s1 = "bbbbb"
out1 = 1

s2 = "pwwkew"
out2 = 3

s3 = "au"
out3 = 2

s4 = "aab"
out4 = 2


class Solution:
	def lengthOfLongestSubstring(self, s: str) -> int:
		"""
		The function to chekc the longest substring in the string 
		Args:
			s: The string value is the longest in the given string
		Return:
			maxLen: The max length of the sub string value 
		"""
		if len(s) == 0:
			return 0
		if len(s) == 1:
			return 1 

		l = 0 
		r = l+1
		maxLength = 0
		mapper = {}
		mapper[s[l]] = True
		length = len(s) - 1
		multiStr = False

		#start the loop

		while r <= length:

			print(r)
			print(mapper)

			if s[r] in mapper:
				tempMax = len(mapper)
				maxLength = max(tempMax,maxLength)
				l = r 
				mapper = {}
				mapper[s[l]] = True
				multiStr = True

			elif r == length and multiStr == False:
				return len(s)
			
			else:
				mapper[s[r]] = True

			r+=1
		return maxLength



sol = Solution()
res = sol.lengthOfLongestSubstring(s4)
print(res)