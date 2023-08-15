"""
make the repaeated string matching in the strings 
"""

test , n = "AGCTGAAAGCTTAGCTG" , 5 
test2 , n2 = "AGAGCTCCAGAGCTTG" , 6
test3 ,n3 = "ATATATATATATATAT" , 6 



class Solution():
	def find_patterns(self,inp_str, nums):
		"""
		The function to find the partterns in the 
		"""

		#the hash map
		mapper = {}  

		# the loop for 
		for i in range(len(inp_str) - n):

			#the pointer
			left = i 
			right  = i + n + 1

			key = inp_str[left:right]

			if key in mapper:
				mapper[key] = mapper[key] + 1

			else:
				mapper[key]  = 0


		for keys in mapper:
			if mapper[keys] !=0:
				print(keys, end=" ")

		return None



if __name__ == "__main__":
	
	sol = Solution()
	res = sol.find_patterns(test3,n3)

	print(res)