"""
The program to find the k largest element in the array
"""

inp = [4,2,9,7,5,6,7,1,3]
k = 4 
out = 6 

#explanation 
"""
sorted array = [1,2,3,4,5,6,7,7,9]
						  4 3 2 1

the fourth largest is the 6
"""


#logic for the finding the largest element 

def find_k_element(arr:list,k:int)->int:
	"""
	The output is the k largest element fron the array
	Args:
		arr: (list) The array of the integers not sorted
	Return:
		largeest_k_pos: (int) The largest kth position integer in the the array
	"""
	
	for x in range(0,k):
		temp_largest = arr[0]
		for i in arr:
			if i >= temp_largest:
				temp_largest = i
		arr.remove(temp_largest)
	return temp_largest
if __name__ == '__main__':
	res = find_k_element(inp,k)
	print(res)

