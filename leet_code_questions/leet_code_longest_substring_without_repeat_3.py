'''
Given a string s, find the length of the longest substring without repeating characters.
Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
Input: s = ""
Output: 0
'''

s = input("Enrter the substring: - ")



class Solution:
    def check_rep(self,left,lst_of_sub):
        self.left = left
        if left in lst_of_sub:
            return True
        else:
            return False

    def lengthOfLongestSubstring(self, s: str) -> int:
        self.s = s
        left = 0
        longest = 0
        lst_of_sub_small = []
        while True:
            if  s!= "" and len(s) == 1:
                longest = 1
                break
            elif s == "":
                longest = 0
                break
            elif left == len(s):
                break
            elif self.check_rep(s[left],lst_of_sub_small) != True:
                lst_of_sub_small.append(s[left])
                print(lst_of_sub_small)
                longest = len(lst_of_sub_small)
                left+=1
            else:
                left = (left - len(lst_of_sub_small) +1 )
                lst_of_sub_small = []

        return longest



ins = Solution()

print(ins.lengthOfLongestSubstring(s))



# a b c a b c b b"
        