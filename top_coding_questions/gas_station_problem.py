"""
The gas station problem  that a car moves and buys petrol and use it to move 
The car should arrive at the same station as the starting point
The gas station has the price and the gas ypu can buy 
add and subtract the price used for the gas 
"""


#the question 
"""
gas = [1,5,3,3,5,3,1,3,4,5]
cost = [5,2,2,8,2,4,2,5,1,2]

algorithm =
start as gas = 0
cost as = 0 


running_cost = 0
running_cost = (gas - cost) + running_cost 

#the algo for the chain

brute force algo 

traverse all the length 
get the length 

make the round logic 

two loops 
for i in range(len(arr)):
	j = i
	count = 0
	whle True:
		#logic for gas calculation
		if gas_calculation is -ve:
			break 
		elif j == len(arr) - 1:
			j = 0
		elif j == i:
			count+=1
		elif j==i and count == 2:
			break
		j+=1

"""

#coding the brute force approach 


#test cases

gas = [1,5,3,3,5,3,1,3,4,5]
cost= [5,2,2,8,2,4,2,5,1,2]



def gas_station(gas:list,cost:list)->int:
	"""
	The function checks for the gas station problem and calculates the gas price and cost
	returns the optimal path based on the calculations
	Args:
		gas: (list) The list of the gas usage
		cost: (list) The list of the cost of the 
	Returns:
		station: (int) The int value of the station
	"""


	length = len(gas)


	for i in range(length - 1):
		j = i
		count,running_sum = 0,0
		while True:
			running_sum = (gas[j] - cost [j]) + running_sum
			if running_sum < 0:
				break
			elif j == length - 1:
				count +=1
				j = 0
			elif j == i and count == 1:
				break
			else:
				j+=1
		if running_sum > 0:
			return i

	return -1


if __name__ == '__main__':
	res = gas_station(gas,cost)
	print(res)




