"""
The problem is grid movemenet for the traveller to reach from the left top to right bottom corner 
The steps are involved are movement down and right to reach the final destination 
"""
#the problem can be solved using the recursion approcah as the movement can be break into the down and right 

def movement_grid_0(m:int,n:int):
	"""
	The movement for the grid is calculated uinsg the recursion approach 
	Args:
		m: (int) The m grid of the board
		n: (int) the n grid of the board
	Return:
		steps: (int) The steps taken by the program to move 
	"""
	if m == 0 or n == 0 :
		return 0
	elif m == 1 and n == 1:
		return 1
	else:
		return movement_grid_0(m-1,n) + movement_grid_0(m,n-1)



def movement_grid_1(m:int,n:int, mapper= {}):
	"""
	The movement for the grid is calculated uinsg the recursion approach 
	Args:
		m: (int) The m grid of the board
		n: (int) the n grid of the board
	Return:
		steps: (int) The steps taken by the program to move 
	"""
	if (m,n) in mapper:
		return mapper[(m,n)]
	elif m == 0 or n == 0 :
		return 0
	elif m == 1 and n == 1:
		return 1
	mapper[(m,n)] = movement_grid_1(m-1,n,mapper) + movement_grid_1(m,n-1,mapper)
	return mapper[(m,n)]



if __name__ == '__main__':
	res_0 = movement_grid_0(18,18)
	res_1 = movement_grid_1(18,18)
	print(res_0)
	print(res_1)