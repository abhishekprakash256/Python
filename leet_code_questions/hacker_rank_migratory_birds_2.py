test_1= [3,4,6,7,7,6,6,6,7,9,9,9]        # 3,4,6,6,6,6,7,7,9
test_2 = [4,6,7,3,3,7,8,0]               #0,3,3,4,6,7,7,8
test_3 = [1,4, 4, 4, 5, 3]
test_4 = [1 ,2, 3, 4, 5, 4, 3, 2, 1, 3, 4]
#-------------greatest element ---------------------------------------------------------------------_#


test_list_1= [[1,3],[6,5],[4,7],[1,9],[1,9],[8,10]]
test_list_2 = [[2,4],[5,5],[3,7],[2,8],[7,2],[1,8],[3,8]]
test_list_3 = [[3, 1], [4, 1],[6, 4], [7, 3], [9, 3]]
test_list_4 = [[2,3],[6,5],[4,5],[5,4]]

def greatest(arr):
    l = len(arr) 
    for i in range(0, l): 
        for j in range(0, l-i-1): 
            if (arr[j][1] > arr[j + 1][1]): 
                tempo = arr[j] 
                arr[j]= arr[j + 1] 
                arr[j + 1]= tempo 
    arr.reverse()  
    #print(arr)     
    new_lst=[]
    if len(arr) == 1:
        return arr
    else:
        for i in range(0, len(arr)):
            if (arr[i][1] > arr[i+1][1]):
                new_lst.append(arr[i])
                break
            elif arr[i][1]== arr[i+1][1]:
                new_lst.append(arr[i])
            else:
                break
    new_lst.sort()
    #print(new_lst)
    if(len(new_lst)>1):
    	for i in range(0,len(new_lst)):
    		if (new_lst[i][0] > new_lst[i+1][0]):
    			return new_lst[[i+1][0]]
    		else:
    			return new_lst[i][0]
    else:
    	return new_lst[0][0]				          



#print(greatest(test_list_4)) 
'''
def migratoryBirds(arr):
	freq_lst = []
	count= 1
	arr.sort()
	for i in range(0,len(arr)-1):
		#print(arr[i])
		if arr[i] == arr[i+1]:
			count+=1
		else:
			freq_lst.append([arr[i],count])
			count =1
	freq_lst.append([arr[len(arr)-1], count])		
	return greatest(freq_lst)			
    







print(migratoryBirds(test_1))'''


#---------------------------------------everything is working exact till now and test cased passed------------------------------------#


#-----------------------------test for the input now ---------------------------------------------------------------#




import math
import os
import random
import re
import sys

# Complete the migratoryBirds function below.
def migratoryBirds(arr):
	freq_lst = []
	count= 1
	arr.sort()
	for i in range(0,len(arr)-1):
		#print(arr[i])
		if arr[i] == arr[i+1]:
			count+=1
		else:
			freq_lst.append([arr[i],count])
			count =1
	freq_lst.append([arr[len(arr)-1], count])		
	return greatest(freq_lst)			
    


if __name__ == '__main__':

    arr_count = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = migratoryBirds(arr)

   

 
print(result)



#-------------------------worked for the submission part----------------------------------------------------#



























