def find_next_empty(puzzle):
    # Finds the next empty cell in the Sudoku grid
    for r in range(9):
        for c in range(9):
            if puzzle[r][c] == -1:
                return r, c
    return None, None

def is_valid(puzzle, guess, row, col):
    # Checks if a guess is valid for a given row, column, and subgrid
    # Check the row
    row_vals = puzzle[row]
    if guess in row_vals:
        return False

    # Check the column
    col_vals = [puzzle[i][col] for i in range(9)]
    if guess in col_vals:
        return False

    # Check the 3x3 grid
    row_start = (row // 3) * 3
    col_start = (col // 3) * 3
    for r in range(row_start, row_start + 3):
        for c in range(col_start, col_start + 3):
            if puzzle[r][c] == guess:
                return False

    return True

def solve_sudoku(puzzle):
    # Solves the Sudoku puzzle using backtracking
    row, col = find_next_empty(puzzle)
    if row is None:
        return True  # Puzzle is solved

    for guess in range(1, 10):  # Numbers 1-9
        if is_valid(puzzle, guess, row, col):
            puzzle[row][col] = guess
            if solve_sudoku(puzzle):
                return True
            puzzle[row][col] = -1  # Reset the cell

    return False

def print_sudoku(puzzle):
    # Prints the Sudoku puzzle in a readable format
    for row in puzzle:
        print(" ".join(str(num) if num != -1 else "." for num in row))

def create_sample_puzzle():
    # A sample Sudoku puzzle with some cells filled
    return [
        [5, 3, -1, -1, 7, -1, -1, -1, -1],
        [6, -1, -1, 1, 9, 5, -1, -1, -1],
        [-1, 9, 8, -1, -1, -1, -1, 6, -1],
        [8, -1, -1, -1, 6, -1, -1, -1, 3],
        [4, -1, -1, 8, -1, 3, -1, -1, 1],
        [7, -1, -1, -1, 2, -1, -1, -1, 6],
        [-1, 6, -1, -1, -1, -1, 2, 8, -1],
        [-1, -1, -1, 4, 1, 9, -1, -1, 5],
        [-1, -1, -1, -1, 8, -1, -1, 7, 9],
    ]

if __name__ == "__main__":
    sudoku_puzzle = create_sample_puzzle()
    print("Initial Sudoku Puzzle:")
    print_sudoku(sudoku_puzzle)

    if solve_sudoku(sudoku_puzzle):
        print("\nSolved Sudoku Puzzle:")
        print_sudoku(sudoku_puzzle)
    else:
        print("\nNo solution exists for the given puzzle.")

    
         
            
        
    
    
    
           