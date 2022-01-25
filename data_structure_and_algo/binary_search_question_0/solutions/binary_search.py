# Iterative Binary Search Function
# It returns index of x in given array arr if present,
# else returns -1
#make test cases 
lst_0 = [1,2,3,4,5,6,7,8,9,10,11]  #the element is present , odd lenth list
element_0 = 2 #not passed

lst_1 = [1,2,3,5,6,7,8,9,12] #elememt not present 
element_1 = 0 #not passed


lst_2 = [1,2,3,5,6,7,8,9,12] #last element 
element_2 = 12 #passed


lst_3 = [1,2,3,5,6,7,8,9,12] #first element
element_3 = 1 #passed


lst_4 = [1,2,3,5,6,6,6,6,6,7,8,9,11] #another element repetative
element_4 = 9 #passed

lst_5 = [1,2,3,5,6,6,6,6,7,8,9,11] #repetative element
element_5 = 6 #passed

lst_6 = [1,2,3,4,5,6,7,8,9,10]  #the element is present , even length of the list
element_6 = 3 #passed


def binary_search(arr, x):
	low = 0
	high = len(arr) - 1
	mid = 0

	while low <= high:

		mid = (high + low) // 2

		# If x is greater, ignore left half
		if arr[mid] < x:
			low = mid + 1

		# If x is smaller, ignore right half
		elif arr[mid] > x:
			high = mid - 1

		# means x is present at mid
		else:
			return mid

	# If we reach here, then the element was not present
	return -1


# Test array

# Function call
result = binary_search(arr = lst_1, x = element_1)

if result != -1:
	print("Element is present at index", str(result))
else:
	print("Element is not present in array")

