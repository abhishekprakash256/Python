"""
make the class for opoerations 
"""

class operations:
	def add(self,nums,running = 0):
		running = nums + running 
		return running

	def mul(self,nums,running = 0 ):
		running  = nums * running 
		return running 

	def div(self,nums,running = 1 ):
		running = running / nums 
		return running

	def sub(self,nums,running = 0):
		running = running - nums
		return running

	def power(self,nums,running = 1 ):
		running = running**nums
		return running




def runner():
	count = 0
	while True:

		inp = int(input("Enter the number : "))
		sign = input("Enter the operation sign: ")
		opr = operations()


		if sign == "+":

			if count == 0:
				res = opr.add(inp)
				count = 1
				
			else:
				res = opr.add(inp,res)

		if sign == "*":
			
			if count == 0:
				res = opr.mul(inp)
				count = 1
				
			else:
				res = opr.mul(inp,res)

		if sign == "/":

			if count == 0:
				res = opr.div(inp)
				count = 1
				
			else:
				res = opr.div(inp,res)

		if sign == "-":

			if count == 0:
				res = opr.sub(inp)
				count = 1
				
			else:
				res = opr.sub(inp,res)

		if sign == "^":

			if count == 0:
				res = opr.power(inp)
				count = 1
				
			else:
				res = opr.power(inp,res)

		

		exit = input("Enter C to exit: ")
		print(res)

		if exit == "C":
			break


if __name__ == "__main__":
	runner()