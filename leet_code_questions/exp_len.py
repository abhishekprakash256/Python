"""
to find the len of the list

"""
inp = "list485"
'''
def break_int(num):
	"""
	The function breaks the integers into digits
	Args:
		inp (int) : the number to break
	Retuns:
		digit (int): the digits of the number 
	"""

	while num:
		#digit = num//100
		num = num // 100
		#@num =  % 100
		print(num % 100) 
		print(num)

	return None
if __name__ == '__main__':
	res = break_int(inp)
	print(res)

'''

blank = ""

new_str= inp.replace(inp[len(inp)-1],"")

print(new_str)


Input = ["flower","flow","flight"]

new_dict ={}
new_dummy ={}

for i in Input:
	new_dummy[i] = i
	new_dict[i] = len(i)

new_dict = (dict(sorted(new_dict.items(), key=lambda item: item[1])))

str_len = len(Input[0])

print(str_len)

first = Input[0]


#the strlength 
print(first[:str_len])