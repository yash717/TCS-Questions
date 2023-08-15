"""
The given problem asks us to generate the first numRows of Pascal's triangle. 
Pascal's triangle is a triangular array of numbers where each number is the sum
of the two numbers directly above it.

"""


"""To solve this problem, we can follow these steps:

Create an empty result list to store the rows of Pascal's triangle.
Iterate numRows times to generate each row of the triangle.
Initialize a current_row list with the first element as 1.
For each row, iterate from index 1 to the current row number (inclusive).
Calculate the current element by summing the elements at index j and j-1 from the previous row.
Append the current element to the current_row list.
Append the current_row list to the result list.
Return the result list containing the first numRows of Pascal's triangle.
Here's the code that implements the above steps with detailed comments:

Keyword arguments:
argument -- description
Return: return_description
"""


"""coding ninja code generator"""


def pascalTriangle(numRows):
    # Step 1: Create an empty result list
    result = []

    # Step 2: Generate each row of Pascal's triangle
    for i in range(numRows):
        current_row = [1]  # Initialize current row with 1

        # Step 4: Calculate elements for current row
        for j in range(1, i):
            current_row.append(result[i-1][j-1] + result[i-1][j])

        # Add 1 at the end of the current row
        if i > 0:
            current_row.append(1)

        # Step 7: Append the current row to the result list
        result.append(current_row)

    # Step 8: Return the result list
    return result
