#Static Test Board
board = [[5, 3, 0, 0, 7, 0, 0, 0, 0],
        [6, 0, 0, 1, 9, 5, 0, 0, 0],
        [0, 9, 8, 0, 0, 0, 0, 6, 0],
        [8, 0, 0, 0, 6, 0, 0, 0, 3],
        [4, 0, 0, 8, 0, 3, 0, 0, 1],
        [7, 0, 0, 0, 2, 0, 0, 0, 6],
        [0, 6, 0, 0, 0, 0, 2, 8, 0],
        [0, 0, 0, 4, 1, 9, 0, 0, 5],
        [0, 0, 0, 0, 8, 0, 0, 7, 9]]

# Method to print the formatted sudoku board
def print_board(board):
    for i in range(len(board)):
        if i > 0: print('')
        if i % 3 == 0 and i != 0: print(' - -' * 8)
        for j in range(len(board[i])):
            if j % 3 == 0 and j != 0: print(' | ', end = '')
            print(f' {board[i][j]} ', end = '')

# Method to iterate through sodoku board and return
# a tuple that the row and column of an empty space
def find_empty(board):
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 0:
                return (i, j)
    return None

# Method to determine whether an input to a 
# sudoku board space is valid
def valid_position(board, num, pos):
    # Checks Columns
    for i in range(len(board)):
        if board[i][pos[1]] == num and pos[0] != i:
            return False
    
    #Checks Rows
    for i in range(len(board[0])):
        if board[pos[0]][i] == num and pos[1] != i:
            return False
    
    #Check Sudoku Box
    box_x, box_y = pos[1] // 3, pos[0] // 3

    for i in range(box_y * 3, box_y * 3 + 3):
        for j in range(box_x * 3, box_x * 3 + 3):
            if board[i][j] == num and (i, j) != pos:
                return False
    
    # After all conditions have been checked, True is returned.
    return True

# Method that implements a backtracking algorithm to solve the board
def solve(board): 
    find = find_empty(board)
    if not find:
        return True
    else:
        row, col = find

    for i in range(1, 10):
        if valid_position(board, i, (row, col)):
            board[row][col] = i
            if solve(board): return True
            board[row][col] = 0
    return False

print_board(board)
print('\n' + '--' * 20)
solve(board)
print_board(board)