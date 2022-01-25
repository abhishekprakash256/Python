'''
find the product of the sum  in the array as for the nested as well
'''

# [5,2[7,-1],3,[6,[-13,8],4]]

# the sum is 12 , nested the value of the M increase 

'''
explanation 

first = 5+2 = 7 , M =1 

second = 6 , M = 2 , 12

third = 3

total = 22

fifth = -5 * 3 = -15 

total sum = 6 + (-15)

-9 + 4 = -5 * 2

= -10 

= 22 -10
= 12
'''

lst_0 = [1,2,3]  #passed
out = 6

lst_1 = [1,2,[2,3]]  #passed
out = 13

lst_2 = [[2,3],3,2] #passed
out = 15

lst_3 = [5,2,[7,-1],3,[6,[-13,8],4]] # passed
out = 12


def sum_product_1(array, mul= 1):

	running_sum = 0 

	for i in range(len(array)):

		if type(array[i]) == list:

			running_sum += sum_product_1(array = array[i] , mul = mul+ 1)

		else:

			running_sum += array[i]

	return running_sum * mul


print(sum_product_1(lst_3))
