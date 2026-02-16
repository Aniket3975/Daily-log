# Recursive Backtracking in Python
=====================================

This script demonstrates the concept of recursive backtracking using N-Queens problem as an example.

```python
def solve_n_queens(n):
    def is_valid(board, row, col):
        # Check if a queen can be placed at position (row, col)
        for i in range(row):
            if board[i] == col or \
                board[i] - i == col - row or \
                board[i] + i == col + row:
                return False
        return True

    def place_queens(n, row, board):
        # Base case: If all queens are placed, print the solution
        if row == n:
            print_board(board)
            return True
        
        for col in range(n):
            # Try to place a queen at position (row, col)
            if is_valid(board, row, col):
                # Place a queen at position (row, col) and recurse
                board[row] = col
                if place_queens(n, row + 1, board):
                    return True
        
        # If no placement is possible, backtrack
        return False

    def print_board(board):
        n = len(board)
        for i in range(n):
            for j in range(n):
                if j == board[i]:
                    print('Q', end=' ')
                else:
                    print('.', end=' ')
            print()

    # Initialize the board
    board = [-1] * n

    # Start placing queens from row 0
    place_queens(n, 0, board)

def main():
    n = int(input("Enter the number of rows: "))
    solve_n_queens(n)

if __name__ == "__main__":
    main()