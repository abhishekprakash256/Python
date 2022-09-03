"""
The program is to find the pallindroim integers 

"""

#test cases 

inp = 121
out = True

inp2 = -121
out2 = False


inp3 = 10 
out3 = False


inp4 = 1
out4 =  True

class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x<0 or (x%10==0 and x//10 != 0):
            return False
        elif x//10 ==0:
            return True
        else:
            org_num = x
            rev_num = 0
            while (org_num > rev_num):
                rev_num = rev_num*10 + org_num % 10
                org_num = org_num //10
                if rev_num == 0:
                    continue
                if org_num/ rev_num < 100 and org_num/ rev_num >= 10 :
                    org_num = org_num // 10
                    break
            if org_num == rev_num:
                return True
            return False
            
