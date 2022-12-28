arr = [1,2,3,4,5,6,7,8,8,9,10]



def divide_arr(arr):
	length = len(arr)
	mid = length // 2
	print(arr)
	if length < 2:
		return arr
	else:
		divide_arr(arr[0:mid])
		divide_arr(arr[mid: length])

#print(divide_arr(arr))


nums0 = [1,2,3]
nums1 = [1,4,5,6,7]


def combine_arr(arr1,arr2):
	length1 = len(arr1) - 1
	length2 = len(arr2) - 1
	final_arr = []
	combine_length = length1+length2

	i , j = 0,0

	while i+j < (length1+length2):
		if arr1[i] == arr2[j] and i != length1 and j !=length2:
			final_arr.append(arr1[i])
			final_arr.append(arr2[j])
			i+=1
			j+=1

		elif arr1[i] < arr2[j] and i != length1 and j !=length2:
			final_arr.append(arr1[i])
			i+=1

		elif arr1[i] > arr2[j] and i != length1 and j !=length2:
			final_arr.append(arr2[j])
			j+=1

		elif i == length1 and j !=length2: 
			final_arr.append(arr1[j])
			j+=1
		elif j == length2 and i !=length1e:
			final_arr.append(arr2[i])
			i+=1

		print(final_arr)

	return final_arr

print(combine_arr(nums0,nums1))