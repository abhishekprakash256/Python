"""
The comon prefexi in the strings from a give list of the strings

"""

#test cases 

Input = ["flower","flow","flight"]
Output: "fl"


Input2 = ["dog","racecar","car"]
Output2: ""

Input3= ["cir","car"]
Output3 = "c"

class Solution:
	def longestCommonPrefix(self, strs: list) -> str:
		"""
		The function to find the common prefix in list of the strings
		Args:
			strs (list) : the list of the strings 
		Returns:
			common_str (str) : the common strings in the given list 
		"""
		new_dict = {}

		for i in strs:
			new_dict[i] = len(i) 

		#sort the dict by the value 

		new_dict = (dict(sorted(new_dict.items(), key=lambda item: item[1])))

		comon_str = list(new_dict.keys())[0]
		for a in new_dict:
			print(a)
			temp_str = ""
			str_len = len(comon_str)
			check_str = a[:str_len]
			print("the check str",check_str)
			if comon_str in check_str:
				temp_str +=comon_str
				print("the str is ",temp_str)
			else:
				comon_str= comon_str.replace(comon_str[len(comon_str)-1],"")
			

		return  comon_str



if __name__ == '__main__':
	soln = Solution()
	res = soln.longestCommonPrefix(Input)
	print(res)