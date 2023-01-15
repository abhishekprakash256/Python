
"""
board = [["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]

output = True



def traverse(board:list)->int:

	for i in range(0,9):
		mapper0 = {}
		
		for j in range(0,9):
			if (board[i][j]) == ".":
				continue
			elif board[i][j] in mapper0:
				return False
			mapper0[board[i][j]] = True

	for k in range(0,9):
		mapper1 = {}
		
		for l in range(0,9):

			if (board[l][k]) == ".":
				continue
			elif board[l][k] in mapper1:
				return False
			mapper1[board[l][k]] = True


	return True


def print_block(board):

	i,j = 0,0

	while i<9 and j<9:
		for a in range(i,i+3):
			for b in range(j,j+3):
				print(board[a][b])





if __name__ == '__main__':
	res = traverse(board)
	res1 = print_block(board)

"""

char = "A"

print(char)