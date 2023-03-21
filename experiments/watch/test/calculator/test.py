"""
make the test calculator function for addition  
"""

def add(nums, running = 0):
	running = nums + running
	return running  

def mul(nums,running = 0 ):
	running  = nums * running 
	return running 

def div(nums,running = 0 ):
	running = running / nums 
	return running

def sub(nums,running =0):
	running = running - nums
	return running


count = 0

while True:

	inp = int(input("Enter the number : "))
	sign = input("Enter the operation sign: ")

	if sign == "+":

		if count == 0:
			res = add(inp)
			count = 1
			
		else:
			res = add(inp,res)

	if sign == "*":
		
		if count == 0:
			res = mul(inp)
			count = 1
			
		else:
			res = mul(inp,res)

	if sign == "/":

		if count == 0:
			res = div(inp)
			count = 1
			
		else:
			res = div(inp,res)

	if sign == "-":

		if count == 0:
			res = sub(inp)
			count = 1
			
		else:
			res = sub(inp,res)


	exit = input("Enter C to exit: ")
	print(res)

	if exit == "C":
		break