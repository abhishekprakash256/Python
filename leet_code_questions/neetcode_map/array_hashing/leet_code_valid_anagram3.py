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


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        countS, countT = {}, {}

        for i in range(len(s)):
            countS[s[i]] = 1 + countS.get(s[i], 0)
            countT[t[i]] = 1 + countT.get(t[i], 0)
        return countS == countT

if __name__ == '__main__':
	sol = Solution()
	res = sol.isAnagram(s4,t4)
	print(res)





