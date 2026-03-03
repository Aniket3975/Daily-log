# Recursive Backtracking in Python

## Introduction

Recursive backtracking is a technique used to solve problems that have overlapping subproblems. It involves recursively exploring different solutions to a problem and backtracking when a dead end is reached.

## The N-Queens Problem

The N-Queens problem is a classic example of a problem that can be solved using recursive backtracking. The goal is to place N queens on an NxN chessboard such that no two queens attack each other.

## The Code

```python
def is_safe(board, row, col, n):
    # Check if it's safe to place a queen at this position
    for i in range(row):
        if board[i] == col or \
           board[i] - i == col - row or \
           board[i] + i == col + row:
            return False
    return True

def solve_n_queens(n, row, board):
    # If we've placed all queens, return the solution
    if row == n:
        return board[:]
    
    # Try to place a queen at this position
    for col in range(n):
        # Check if it's safe to place a queen at this position
        if is_safe(board, row, col, n):
            # Place a queen at this position
            board[row] = col
            # Recursively try to place the remaining queens
            solution = solve_n_queens(n, row + 1, board)
            # If we found a solution, return it
            if solution:
                return solution
            # If we didn't find a solution, backtrack
            board[row] = -1
    
    # If we couldn't place a queen at this position, return None
    return None

# Example usage
n = 4
board = [-1] * n
solution = solve_n_queens(n, 0, board)
if solution:
    print("Solution found:")
    for row in range(n):
        for col in range(n):
            if board[row] == col:
                print('Q', end=' ')
            else:
                print('.', end=' ')
        print()
else:
    print("No solution found")