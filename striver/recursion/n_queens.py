def solveNQueens(self, n):
    def DFS(queens, xy_dif, xy_sum):
        # p represents the current row, which is the length of the queens list.
        p = len(queens)
        # If we've placed queens in all rows (p equals n), we found a solution.
        if p == n:
            result.append(queens)
            return None
        for q in range(n):
            # Check if it's safe to place a queen in column q of the current row p.
            if q not in queens and p - q not in xy_dif and p + q not in xy_sum:
                # Recursively call DFS to explore the next row with the new queen placement.
                DFS(queens + [q], xy_dif + [p - q], xy_sum + [p + q])

    result = []  # Initialize a list to store the solutions
    DFS([], [], [])  # Start the depth-first search with empty lists
    # Convert the solutions into the required format:
    # Each solution is represented as a list of strings, where 'Q' represents a queen.
    return [["." * i + "Q" + "." * (n - i - 1) for i in sol] for sol in result]
