# Recursive Backtracking in Python

def solve_sudoku(board):
    """
    Solves a Sudoku puzzle using recursive backtracking.

    Args:
        board (list): A 2D list representing the Sudoku board.
            0 represents an empty cell, and 1-9 represent numbers.

    Returns:
        bool: True if the puzzle is solved, False otherwise.
    """

    def is_valid(num, row, col):
        """
        Checks if a number can be placed in a given position on the board.

        Args:
            num (int): The number to check.
            row (int): The row index of the cell.
            col (int): The column index of the cell.

        Returns:
            bool: True if the number is valid, False otherwise.
        """
        # Check the row and column for duplicates
        for i in range(9):
            if board[row][i] == num or board[i][col] == num:
                return False

        # Check the 3x3 box for duplicates
        start_row, start_col = row - row % 3, col - col % 3
        for i in range(3):
            for j in range(3):
                if board[i + start_row][j + start_col] == num:
                    return False

        # If no duplicates are found, the number is valid
        return True


    def solve():
        """
        Solves the Sudoku puzzle using recursive backtracking.

        Returns:
            bool: True if the puzzle is solved, False otherwise.
        """
        for i in range(9):
            for j in range(9):
                # If an empty cell is found, try numbers from 1 to 9
                if board[i][j] == 0:
                    for num in range(1, 10):
                        # Check if the number is valid at this position
                        if is_valid(num, i, j):
                            # Place the number on the board
                            board[i][j] = num

                            # Recursively try to fill in the rest of the board
                            if solve():
                                return True

                            # If the recursive call fails, reset the cell and try the next number
                            board[i][j] = 0

        # If all cells are filled without finding a solution, return False
        return False


    # Start solving the puzzle from the beginning
    return solve()


# Example usage:
board = [
    [5,3,0,0,7,0,0,0,0],
    [6,0,0,1,9,5,0,0,0],
    [0,9,8,0,0,0,0,6,0],
    [8,0,0,0,6,0,0,0,3],
    [4,0,0,8,0,3,0,0,1],
    [7,0,0,0,2,0,0,0,6],
    [0,6,0,0,0,0,2,8,0],
    [0,0,0,4,1,9,0,0,5],
    [0,0,0,0,8,0,0,7,9]
]

if solve_sudoku(board):
    # Print