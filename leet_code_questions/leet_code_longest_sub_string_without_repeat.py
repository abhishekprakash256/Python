"""
The program to find the longest substing withoy the repeat of the same letter 

Example-

in = aaaaa 
out = 5

in = abbcbbs
out = 2

in = pwwkew
out = 3 wke

"""


#test cases 

in1 = "aaaaa"
out = 1

in2 = "abbcbbs"
out2 = 2

in3 = "pwwkew"
out3 = 3

in4 = "a"
out4 = 1

in5 = "pwwjewwtdh"
out5 = 4

in6 = ""
out6 = 0

in7 = "dvdf"
out7 = 4


class Solution:
	def check_repeat(self,sub_s, right_char):
		"""
		The function to check the string repeating
		Args:
			sub_s (str): the substring to check
		Return
			True or False (bool) : the 

		"""
		if right_char in sub_s:
			return False
		else:
			return True



	def lengthOfLongestSubstring(self, s: str) -> int:
		"""
		The function takes the string as input and give the longest output as the substring
		Args:
			s (str):  the string as input
		Return :
			lonng_str (int) : The longest substr length
		"""

		#the length is set to 0
		
		left = 0 #the left pointer
		right = left +1 #the right pointer

		max = 1  #get the max 

		cur_max = 1  #set the max value 

		#legth of the string
		length_str = len(s)

		if length_str == 0:
			return 0
		
		while right <= length_str -1 :

			#check the repeatative string in the substring
			if self.check_repeat(s[left:right], s[right]):
				max = right - left + 1
				right +=1

				#retatin the max value
				if max > cur_max:
					cur_max = max

			#change the left if equal character is there
			else:
				left = left+1 
				right = left + 1
				max =1

		return cur_max



if __name__ == '__main__':
	soln = Solution()
	res = soln.lengthOfLongestSubstring(in5)
	print(res)




