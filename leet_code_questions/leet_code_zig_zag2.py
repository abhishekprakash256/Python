"""
the question is to convert a string to zig zag and print the result 
as a straight string format 
"""

#test cases

inp = "PAYPALISHIRING"
nrows = 3
out = "PAHNAPLSIIGYIR"


inp2 = "PAYPALISHIRING"
nrows2 =  4
out2 = "PAHNAPLSIIGYIR"



class Solution:
    def convert(self, s: str, numRows: int) -> str:
    	"""
    	The funtions returns the strring chnaged as per rows
    	Args:
    		s (str) : the string that is manupulated
    		numRows (int) : the number of the rows split

    	returns :
    		ordered_str (str) : the string rerranged as the number of rows
    	"""





    	return s

if __name__ == "__main__":
	soln = Solution()
	res = soln.convert(inp,nrows)
	print(res)

