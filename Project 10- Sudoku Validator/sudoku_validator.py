def validate_sudoku(board):
    valid = {1,2,3,4,5,6,7,8,9}
    for row in board:
        if set(row) != valid:
            return False
    col = set()
    for i in range(9):
        for j in range(9):
            col.add(board[j][i])
        if col != valid:
            return False
        col.clear()
    i, j, k = 0, 1, 2
    start = 0
    square = set()
    for rects in range(3):
        for col in range(2, 9, 3):
            square.update(set(board[i][start:col+1]))
            square.update(set(board[j][start:col+1]))
            square.update(set(board[k][start:col+1]))
            if square != valid:
                return False
            start += 3
            square.clear()
        i+=3
        j+=3
        k+=3
        start = 0
    return True

board1 =    [[1,2,3,4,5,6,7,8,9],
		     [1,2,3,4,5,6,7,8,9],
			 [1,2,3,4,5,6,7,8,9],
			 [1,2,3,4,5,6,7,8,9],
		     [1,2,3,4,5,6,7,8,9],
		     [1,2,3,4,5,6,7,8,9],
			 [1,2,3,4,5,6,7,8,9],
	         [1,2,3,4,5,6,7,8,9],
			 [1,2,3,4,5,6,7,8,9]]
    
board2 =    [[1,1,1,1,1,1,1,1,1],
			 [2,2,2,2,2,2,2,2,2],
			 [3,3,3,3,3,3,3,3,3],
			 [4,4,4,4,4,4,4,4,4],
			 [5,5,5,5,5,5,5,5,5],
			 [6,6,6,6,6,6,6,6,6],
			 [7,7,7,7,7,7,7,7,7],
			 [8,8,8,8,8,8,8,8,8],
			 [9,9,9,9,9,9,9,9,9]]

board3 =    [[5,3,4,6,7,8,9,1,2],
			 [6,7,2,1,9,5,3,4,8],
		     [1,9,8,3,4,2,5,6,7],
			 [8,5,9,7,6,1,4,2,3],
		     [4,2,6,8,5,3,7,9,1],
			 [7,1,3,9,2,4,8,5,6],
			 [9,6,1,5,3,7,2,8,4],
			 [2,8,7,4,1,9,6,3,5],
			 [3,4,5,2,8,6,1,7,9]]

for board in (board1, board2, board3):
    print(validate_sudoku(board))