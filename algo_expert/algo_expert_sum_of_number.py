''' The question is to find the sum of the number in the array as per given, find the pair of number the number
[3,5,-4,8,11,1,-1,6] -> 10
11,-1

soln -- it is that to traverse the array twice with for loop and find the sum of the elenents that match the sum given, complecity - O(n^2)

optimal soln by Hash Table--


'''

arr_len = int(input("Entert the length of array: "))	
lst= []
for x in range(0,arr_len):
	x =int(input("Enter the element of array: "))
	lst.append(x)


sum =  (int(input("Enter the sum: ")))
'''
def sum_of_num_array(arr,given_sum):	
	for i in range(0,len(arr)-1):
		for j in range(i+1,len(arr)):
			if ((arr[i]) + (arr[j])) == given_sum:
				return arr[i], arr[j]
			else:
				continue	

	return 0'''


#---------------------------------------------------------using the two pointer method to find the sum
'''def sum_of_num_array(arr,given_sum):
	arr.sort()
	left_point = 0
	right_point = len(arr) -1
	while left_point < right_point :
		curr_sum = arr[left_point] + arr[right_point] 
		if curr_sum == given_sum:
			return arr[left_point], arr[right_point]
		elif curr_sum < given_sum:
			left_point+=1
		elif curr_sum > given_sum:
			right_point-=1
		else:
			return 0	'''		

	


#------------------------------------------------using the hash map ------------------------------------------------------------#

def sum_of_num_array(arr,given_sum):
	new_dst ={}
	for num in arr:
		match = sum - num
		if match in arr:
			return match, num
		else:
			new_dst[num] = True
	return 0	







print(sum_of_num_array(lst,sum))










