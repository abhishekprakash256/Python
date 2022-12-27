"""
The programn to find the valid anagram
A annagram is a string formed by rearranging the letter from the same string
An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.
"""

"""
if the len(0) return False
using a set can be helpful
loop through the orignal:
 store in set 

compare created with set 

return True or  False
"""
#works but not effective much 


#test cases 
s0 = "test"
t0 = "set"  #False

s1 = "testt"
t1 = "test" #True

s2 = "car"
t2 = "rat" #false

s3 = "anagram"
t3 = "nagaram"

s4 = "a"
t4 = "ab"

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
    	"""
    	Check if the string is an anagram or not
		Args:
			s : (str) the oringial string
			t : (str) the anagram string
		Return
			True or False : (bool) The string is annagram or not
    	"""
    
    	return sorted(s) == sorted(t)


if __name__ == '__main__':
	sol = Solution()
	res = sol.isAnagram(s3,t3)
	print(res)
