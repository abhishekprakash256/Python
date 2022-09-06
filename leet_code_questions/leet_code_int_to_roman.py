"""
convert the int to roman 
Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000


I can be placed before V (5) and X (10) to make 4 and 9. 
X can be placed before L (50) and C (100) to make 40 and 90. 
C can be placed before D (500) and M (1000) to make 400 and 900.
"""
#test cases 

inp = 1
out = "I"

inp2 = 2
out2 = "II"

inp3 = 10 
out3 = "X"

inp4 = 11
out4 = "XI" 

inp5 = 20
out5 = "XX"

inp6 = 50
out6 = "IL" 
 

inp7 = 58
out7 = "LVIII"


inp8 = 1994
out8 = "MCMXCIV"

class Solution:
    def intToRoman(self, num: int) -> str:
        thousands=["","M","MM","MMM"]
        hundreds=["","C","CC","CCC","CD","D","DC","DCC","DCCC","CM"]
        tens=["",'X','XX','XXX','XL','L','LX','LXX','LXXX','XC']
        ones=["","I","II","III","IV","V","VI","VII","VIII","IX"]
        t=thousands[num//1000]
        num=num%1000
        h=hundreds[num//100]
        num=num%100
        ten=tens[num//10]
        num=num%10
        o=ones[num%10]
        return t+h+ten+o

if __name__ == '__main__':
	soln = Solution()
	res = soln.intToRoman(inp8)
	print(res)

