test_1 = [3,10,2,9]
x_1, y_1= 1, 12    #output 5
test_2 = [3,10,2,9]
x_2, y_2= 1,7      #output Bon Apettit
test_3 = []
#x_3,y_3=
test_4 = []
#x_4, y_4=

'''     
def bonAppetit(bill,k,b):     #k not eaten part 
	#return ("hello")            # money that is given
	new_lst= []
	for i in range(0, len(bill)):
		if (bill[i] == bill[k]):           #find the element and skip it
			continue
		else:
			new_lst.append(bill[i])          #appending to the new lst
	sum = 0 
	for i in new_lst:            #sum part the addition 
		sum += i 
	#print(new_lst)	
	div= (sum/2)
	
	if (b- div >0 ):
		return (int(b- div))
	else:
		return "Bon Apettit"				
			
print(bonAppetit(test_2,x_2,y_2))'''




#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the bonAppetit function below.
def bonAppetit(bill, k, b):
    new_lst= []
    for i in range(0, len(bill)):
        if (bill[i] == bill[k]):           #find the element and skip it
            continue
        else:
            new_lst.append(bill[i])          #appending to the new lst
    sum = 0 
    for i in new_lst:            #sum part the addition 
        sum += i 
    #print(new_lst)    
    div= float(sum/2)
    
    if ((b- div) >0 ):
        
        x= float(b-div) 
        print(int(x))
    else:
        
        print("Bon Apettit")


if __name__ == '__main__':

    nk = input().rstrip().split()

    n = int(nk[0])

    k = int(nk[1])

    bill = list(map(int, input().rstrip().split()))

    b = int(input().strip())

    bonAppetit(bill, k, b)
































