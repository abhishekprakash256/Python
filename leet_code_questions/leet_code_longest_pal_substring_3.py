'''
Given a string s, return the longest palindromic substring in s.
Input: s = "babad"
Output: "bab"
Note: "aba" is also a valid answer.
'''


#failed attemt to make the optimized soltions 

s= input("Enter the string : ")


class Solution:
	global pal_lst, x
	global a 
	pal_lst = []
	x= ""
	a= 0
	def check_pal(self,out):
		if out == out[::-1]:
			ret =True
		else:
			ret =False
		return ret
	def trim_fun(self,s):
		global x
		for b in s:
			if b == '"':
				continue
			else:
				x+=b
		return x

	def longestPalindrome(self, x: str) -> str:
		global a , pal_lst
		self.x = x
		stor_len = 0
		for i in range(len(x)):
			i,j = i, len(x)-1 
			while True:
				if x[i] == x[j]: 
					check = self.check_pal(x[i:j+1])
					if stor_len  < len(x[i:j+1]):
						stor_len = len(x[i:j+1])
						if check == True :
							pal_lst.append(x[i:j+1])
							break
						else:
							j-=1

					else:
						j-=1
				else:
					break
		for a in range(0,len(pal_lst)-1):
			if len(pal_lst[a]) > len(pal_lst[a+1]):
				pal_lst[a+1] = pal_lst[a]
			else:
				continue

		return pal_lst[a]




			





test_1 = Solution()

#print(test_1.check_pal(s))	

print(test_1.longestPalindrome(s))

#print(test_1.trim_fun(s))

    





#S E F E G E F E G H

#H G E F E G E F E S  