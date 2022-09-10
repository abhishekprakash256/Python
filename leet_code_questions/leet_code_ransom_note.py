"""
the ransom note problem of the leet code
if the string can be construted using the other string 
"""

#test case 
ransomNote = "a"
magazine = "b"
Output = False

ransomNote2 = "aa"
magazine2 = "ab"
Output2 = False

ransomNote3 = "aa"
magazine3 = "aab"
Output3 = True


class Solution:
	def canConstruct(self, ransomNote: str, magazine: str) -> bool:
		"""
		The function to find the similar string in the two strings
		Args: 
			ransomNOte (str) : the first string 
			magazine (str) : the secomd string 
		Returns:
			true or false (bool) : the value if corret or not 
		"""
		if ransomNote in magazine:
			return True
		else:
			return False
		

if __name__ == '__main__':
	soln = Solution()
	res = soln.canConstruct(ransomNote3, magazine3)
	print(res)