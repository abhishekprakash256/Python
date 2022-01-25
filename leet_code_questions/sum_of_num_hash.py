#print("the hash of 34", hash(34))

#print("the hash of the 56.78", hash(56.78))

test_lst= [2,3,5]

test_lst_2 = [2,4,6,7]

test_lst_3 = [3,5,7,9, 10.34]

test_lst_4 = [3,3]


#--------------------------------making the dictionary with the hash table-------------------#

import time

def sun_num(arr, target):
	my_dict = dict()
	#print(time.time())
	for i in range(0,len(arr)):
		my_dict.update({arr[i]: hash(arr[i])})
	for i in range(0,len())





print(sun_num(test_lst_3,3))