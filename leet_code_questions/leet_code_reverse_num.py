num = (input("Enter the num for reverse: "))


'''lst= []
lst_3 = []
#first remove the zero part
#then do the sign part
if num[len(num)-1] == "0":  #optimize the first condition with regex
	lst_2 = ["-"]
	for i in range(0,len(num)):
		lst.append(num[i])
	lst.remove(num[len(num)-1])
	if (lst[0] == "-"):
		lst.remove(lst[0])	
		lst.reverse()	
		lst = lst_2+lst
	else:
		lst.reverse()	

else:
	lst_2 = ["-"]
	for i in range(0 ,len(num)):
		lst.append(num[i])
	if (lst[0] == "-"):
		lst.remove(lst[0])	
		lst.reverse()	
		lst = lst_2+lst
	else:
		lst.reverse()	

	
		
for i in lst:
	print(i, end= "")'''		


def reverse_1(x):
	lst= []
	if x[len(x)-1] == "0":  #optimize the first condition with regex
		lst_2 = ["-"]
		for i in range(0,len(x)):
			lst.append(x[i])
		lst.remove(x[len(x)-1])
		if (lst[0] == "-"):
			lst.remove(lst[0])	
			lst.reverse()	
			lst = lst_2+lst
		else:
			lst.reverse()	

	else:
		lst_2 = ["-"]
		for i in range(0 ,len(x)):
			lst.append(x[i])
		if (lst[0] == "-"):
			lst.remove(lst[0])	
			lst.reverse()	
			lst = lst_2+lst
		else:
			lst.reverse()
	str1= ""
	return (str1.join(lst))

	

print(reverse_1(num))			





#program working in the local machine as expected but, in leetcode the code is working in "runcode" failing in the "submit" getting runtime error

'''def find_rev(n, rev):
    if n%10 == 0 :
        return(find_rev(n//10, 0))
    else:
        while n>0:
            a = n%10
            rev = rev * 10 + a
            n = n//10
        return(rev)

n = int(input())
if n < 0 : 
    print(find_rev(n*-1,0)*-1)
else:
    print(find_rev(n,0))'''






