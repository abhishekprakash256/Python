import time

nums = list(map(int, input().rstrip().split()))

target = int(input("Enter the sum of the digit: "))

def twoSum(arr, sum):
	new_lst=[]
	print(time.time())
	for i in range(0, len(arr)):
		for j in range(i+1,len(arr)):
			if(arr[i] + arr[j] == sum):
				new_lst.append(i)
				new_lst.append(j)
			else:
				continue	
			
	return new_lst , time.time()




print(twoSum(nums,target))