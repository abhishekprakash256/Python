'''
find the largest three numbers in the array and return it 
return the list of three numbers, in sorted array increasing order
'''

test_0 = [2,3,5,1,1,4,6,8]  #pass
out_0 = [5,6,8]


test_1 = [1,1,1,1,1,1,1] # pass
out_1 = [1,1,1]


test_2 = [2,5,1,1,2,2,8]  #pass
out_2 = [2,5,8]

test_3 = [5,5,5,5,1,1,1,0] #pass
out_3 = [0,1,5]

test_4 = [9,1,1,2,2] #pass
out_4 = [1,2,9]

test_5 = [1,1,1,1,1,1,1,2] # pass
out_5 = [1,1,2]


def findThreeLagestNumbers(array):
	threeLargest = [None, None, None]
	for num in array:
		updateLargest(threeLargest, num)

	return threeLargest


def updateLargest(threeLargest, num):
	if threeLargest[2] is None or num > threeLargest[2]:
		shiftAndUpdate(threeLargest , num , 2)
	elif threeLargest[1] is None or num > threeLargest[1]:
		shiftAndUpdate(threeLargest, num, 1)
	elif threeLargest[0] is None or num > threeLargest[0]:
		shiftAndUpdate(threeLargest, num, 0)

def shiftAndUpdate(array, num, idx):

	for i in range(idx + 1):

		if i == idx :
			array[i] = num
		else:

			array[i] =  array[i+1]

print(findThreeLagestNumbers(test_5))