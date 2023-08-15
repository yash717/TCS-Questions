"""
The given code implements an alternative approach to rotate an n x n 2D matrix in place.
It transposes the matrix first and then reverses each row to achieve the rotation.

Let's go through each line of the code and provide an explanation:

The code defines a function rotate that takes a 2D matrix matrix as input.
The function returns None since it modifies the matrix in-place.
It initializes n as the length of the matrix, assuming it is a square matrix.


The code performs matrix transposition by swapping elements across the main diagonal of the matrix.
It iterates through the rows and columns where i represents the row index and j represents the column index.
Each element matrix[i][j] is swapped with the corresponding element matrix[j][i] using tuple packing and unpacking.


The code reverses each row of the matrix after the transposition step.
It iterates through each row of the matrix.
The reverse() method is used to reverse the order of elements in each row.
Overall, the code first performs a matrix transposition by swapping elements across the main diagonal. Then, it reverses each row of the transposed matrix, effectively achieving the 90-degree clockwise rotation.

Note: The code assumes that matrix is a square matrix (n x n) and n is the length of each row in the matrix.
"""
# THIS CODE IS FOR ROTATING AN IMAGE

from os import *
from sys import *
from collections import *
from math import *
from typing import List


def rotate(matrix: List[List[int]]) -> None:
    n = len(matrix)
    # Transposing the matrix
    for i in range(n):
        for j in range(i):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        # Reversing each row of the matrix
    for i in range(n):
        matrix[i].reverse()


# CODING NINJA SOLUTION COZ OF ROTATE MATRIX
"""
The given problem asks us to rotate the elements of a 2-dimensional matrix clockwise.
We need to modify the given matrix in place to reflect the rotated elements.

To solve this problem, we can use a layer-by-layer approach. Starting from the outermost layer,
we will rotate the elements in a clockwise direction by swapping them in a cyclic manner.

Here's a step-by-step explanation of the approach:

Initialize four variables top, bottom, left, and right to keep track of the boundaries of the current layer.

Iterate through the layers of the matrix.
We can determine the number of layers as the minimum of n // 2 and m // 2 (integer division).

For each layer, perform the rotation:

Store the value of the top row.
Move the left column to the top row.
Move the bottom row to the left column.
Move the right column to the bottom row.
Move the stored top row value to the right column.
After the rotation is complete, the matrix will be modified in place with the rotated elements.

Here's the code that implements the above steps with detailed comments:
"""


def rotateMatrix(mat, n, m):
    # Step 1: Initialize variables
    top = 0
    bottom = n - 1
    left = 0
    right = m - 1

    # Step 2: Iterate through the layers
    while top < bottom and left < right:
        # Step 3: Perform the rotation
        prev = mat[top + 1][left]  # Store the value of the top row

        # Move the left column to the top row
        for i in range(left, right + 1):
            curr = mat[top][i]
            mat[top][i] = prev
            prev = curr

        top += 1

        # Move the bottom row to the left column
        for i in range(top, bottom + 1):
            curr = mat[i][right]
            mat[i][right] = prev
            prev = curr

        right -= 1

        # Move the right column to the bottom row
        for i in range(right, left - 1, -1):
            curr = mat[bottom][i]
            mat[bottom][i] = prev
            prev = curr

        bottom -= 1

        # Move the stored top row value to the right column
        for i in range(bottom, top - 1, -1):
            curr = mat[i][left]
            mat[i][left] = prev
            prev = curr

        left += 1

    # No need for explicit return as the matrix is modified in place
