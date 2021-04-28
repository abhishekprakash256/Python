#------------------------print 1 to 100 without a loop 



def printer(num):
	
	if  num<101:
		print(num)
		num = num +1
		printer(num)
	
	elif num ==100 :
		return 100 

print(printer(1))	