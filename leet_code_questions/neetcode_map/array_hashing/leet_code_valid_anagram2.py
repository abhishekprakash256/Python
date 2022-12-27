"""
The code to check the valid anagram 
"""



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


#using the set data structure can't be done 


#--------------------------------wrong solution----------------------------------------------

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

    	anagram_set = set()
    	original_set = set()

    	if len(s) != len(t):
    		return False

    	for i,j in zip(s,t):
    		original_set.add(i)
    		anagram_set.add(j)

    	if original_set == anagram_set:
    		return True
    	else:
    		return False


if __name__ == '__main__':
	sol = Solution()
	res = sol.isAnagram(s4,t4)
	print(res)