"""The problem requires us to modify a given matrix in-place such that if an element in the matrix is 0, 
we set its entire row and column to 0.

To solve this problem, we can follow these steps:

Create two sets, zero_rows and zero_cols, to keep track of the rows and columns that contain 0's.
Iterate through the matrix and whenever we encounter a 0 at matrix[i][j], add i to zero_rows and j to zero_cols.
Iterate through the matrix again and if either the current row i or the current column j is present in zero_rows or zero_cols respectively,
set matrix[i][j] to 0.
Return the modified matrix.

Keyword arguments:
argument -- description
Return: return_description
"""
"""coding ninja code"""




from os import *
from sys import *
from collections import *
from math import *
def zeroMatrix(matrix, n, m):
    zero_rows = set()
    zero_cols = set()

    # Step 1: Find the rows and columns with 0's
    for i in range(n):
        for j in range(m):
            if matrix[i][j] == 0:
                zero_rows.add(i)
                zero_cols.add(j)

    # Step 3: Set rows and columns to 0 if either the row or column contains a 0
    for i in range(n):
        for j in range(m):
            if i in zero_rows or j in zero_cols:
                matrix[i][j] = 0

    return matrix


"""You can use this code by passing the matrix as a 2D list along with the number of rows n and columns m as arguments to the zeroMatrix function. The function will modify the matrix in place and return the modified matrix.

Note: The code assumes that the input matrix is a valid 2D list with the given constraints."""


"""leetcode code"""


class Solution(object):
    def setZeroes(self, matrix):
        # Step 1: Initialize sets to keep track of rows and columns with zeros
        zero_rows = set()
        zero_cols = set()

        # Step 2: Find the positions of zeros in the matrix
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    zero_rows.add(i)
                    zero_cols.add(j)

        # Step 3: Set corresponding rows and columns to zero
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if i in zero_rows or j in zero_cols:
                    matrix[i][j] = 0

        # The matrix is modified in place, so no explicit return is needed
