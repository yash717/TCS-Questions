# leetcode solution

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


# coding ninja code

def solveNQueens(n):
    # Define a depth-first search (DFS) function to find solutions
    def DFS(queens, xy_diff, xy_sum):
        p = len(queens)  # Current row (depth of the search)

        # If all queens are placed (the base case), add the current configuration to the result
        if p == n:
            result.append(queens)
            return None

        # Try placing a queen in each column of the current row
        for q in range(n):
            # Check if it's safe to place a queen at this position
            if q not in queens and p - q not in xy_diff and p + q not in xy_sum:
                # If safe, recursively explore the next row
                DFS(queens + [q], xy_diff + [p - q], xy_sum + [p + q])

    result = []  # Initialize a list to store solutions
    DFS([], [], [])  # Start DFS with empty configurations

    # Convert the solutions into the desired format
    formatted_result = []
    for sol in result:
        formatted_sol = [
            ['1' if col == i else '0' for i in range(n)] for col in sol]
        formatted_result.append([' '.join(row) for row in formatted_sol])

    return formatted_result  # Return the list of solutions in the specified format


# Example usage:
n = 4
solutions = solveNQueens(n)
for sol in solutions:
    for row in sol:
        print(row)
    print()
