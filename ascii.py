
#PROJEECT --> POETJCJR
#input one string to be jumbleb 
#input two the method to be used.

word = list(map(str, input().rstrip().split()))

method = int(input("Enter the sum of the digit: "))

def jumbed(arr,num):
	
	if (num == 1):

		for i in range(0, len(arr),2):
			print(arr[i])  #store the value
		arr.reverse()	
		for i in (range(1,len(arr),2)):
			print(arr[i])

	else:
		for i in range(0,len(arr),2):
			print(arr[i])
		for i in range(1,len(arr),2):
			print(arr[i])			


print(jumbed(word,method))
