"""
The leet code question is to reverse the string in the context

"""

inp = 123
out = 321


inp2 = -123
out2 = -321

inp3 = 120
out3 = 21


inp4 = 1
out4 = 1

inp5 = 21
out5 = 12


inp6 = -120
out6 = -21


#make the solution 

import math
class Solution:
	def reverse(self, x: int) -> int:
		"""
		The function takes the int and reverse it
		Args:
			x (int) : the given integers
		Returns:
			rev_x (int) : reverse integer

		"""
		
		while x:
			digit = int(math.fmod(x,10))
			x= int(x/10)
			print(x)

		return None



if __name__ == '__main__':
	soln = Solution()
	res = soln.reverse(inp)
	print(res)