num = int(input())



def bin(num):
	lst = []
	while(num >1):
	
		lst.append(num%2)
		num= int(num/2)
	
	lst.append(num%2)
	lst.reverse()
	return lst


print(bin(num))