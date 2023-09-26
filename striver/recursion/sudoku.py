class Solution(object):
    def solveSudoku(self, board):
        # Helper function to check if it's valid to place 'num' at board[row][col]
        def is_valid(row, col, num):
            # Check if 'num' is not present in the same row or column
            for i in range(9):
                if board[i][col] == num or board[row][i] == num:
                    return False
            # Check the 3x3 subgrid
            start_row, start_col = 3 * (row // 3), 3 * (col // 3)
            for i in range(start_row, start_row + 3):
                for j in range(start_col, start_col + 3):
                    if board[i][j] == num:
                        return False
            return True

        # Recursive function to solve the Sudoku puzzle
        def solve(row, col):
            # Base case: If we've filled all rows, the puzzle is solved.
            if row == 9:
                return True

            # Move to the next cell
            if col == 8:
                next_row, next_col = row + 1, 0
            else:
                next_row, next_col = row, col + 1

            # If the cell is already filled, move to the next cell.
            if board[row][col] != ".":
                return solve(next_row, next_col)

            # Try placing each digit from '1' to '9'
            for num in map(str, range(1, 10)):
                if is_valid(row, col, num):
                    board[row][col] = num  # Place the digit

                    if solve(next_row, next_col):
                        return True  # If a solution is found, stop recursion

                    board[row][col] = "."  # Backtrack if no solution found

            return False  # No valid digit found

        solve(0, 0)  # Start solving from the top-left cell
