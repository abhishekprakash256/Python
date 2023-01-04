"""
Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:

	Each row must contain the digits 1-9 without repetition.
	Each column must contain the digits 1-9 without repetition.
	Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.

Note:

	A Sudoku board (partially filled) could be valid but is not necessarily solvable.
	Only the filled cells need to be validated according to the mentioned rules.

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


#the solution doesn't work


class Solution:
	def isValidSudoku(self, board: list) -> bool:
		"""
		The function takes the list of the board and check for the valid board
		args:
			board: (list) the input board list of the integers
		Return:
			True or False: (bool) The board is valid or not 
		"""
		#the logic for the row checking
		for i in range(9):
			map_digits_row = {}
			map_digits_column = {}
			for j in range(9):
				if board[i][j] == ".":
					continue
				elif board[i][j] in map_digits_row and board[j][i] in map_digits_column:
					return False
				map_digits_row[board[i][j]] = True
				map_digits_column[board[j][i]] = True
				print(map_digits_row)
				print(map_digits_column)
				

		#the logic for the column checking
		"""
		for k in range(9):
			map_digits_column = {}
			for l in range(9):
				if board[l][k] == ".":
					continue
				elif board[l][k] in map_digits_column:
					return False
				map_digits_column[board[l][k]] = True

		#the logic for the 3X3 grid  """
		return True



if __name__ == '__main__':
	sol = Solution()
	res = sol.isValidSudoku(board)
	print(res)