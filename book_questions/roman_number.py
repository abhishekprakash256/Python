"""
function to print the roman numbers from a list

chapter 3 , Question 14

"""


def print_roman(number: int) -> str:
	"""
	The function will takes the value of the num and prints the respective roman number

	Arguments:
		num (int) -> The integer value of the number
	Return:
		roman_num (str) -> the string roman number
	"""

	#look_up = {1:"I",4:"IV", 5:"V", 9:"IX", 10:"X", 40:"XL", 50:"L",90:"XC", 100:"X", 400: "CD", 500:"D" ,900 : "CM" , 1000:"M"}
    
	num = [1, 4, 5, 9, 10, 40, 50, 90,100, 400, 500, 900, 1000]
    
	sym = ["I", "IV", "V", "IX", "X", "XL","L", "XC", "C", "CD", "D", "CM", "M"]


	i = 12
      
	while number:
		div = number // num[i]

		number %= num[i]
  
		while div:
			print(sym[i], end = "")
			div -= 1
		
		i -= 1

	return ""


print(print_roman(56))