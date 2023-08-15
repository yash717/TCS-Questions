"""
The problem asks to determine if a given target integer exists in a matrix with the following properties:

Each row of the matrix is sorted in non-decreasing order.
The first integer of each row is greater than the last integer of the previous row.
To solve the problem efficiently in O(log(m * n)) time complexity, we can utilize the properties of the matrix and perform a binary search.

Here's the code with step-by-step explanations:"""


class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix or not matrix[0]:
            return False  # Empty matrix, return False

        rows = len(matrix)
        cols = len(matrix[0])

        # Binary search implementation
        left = 0
        right = rows * cols - 1  # Treat the matrix as a 1D array

        while left <= right:
            mid = (left + right) // 2
            # Calculate the element in the matrix based on the 1D index
            num = matrix[mid // cols][mid % cols]

            if num == target:
                return True  # Found the target

            if num < target:
                left = mid + 1  # Target is in the right half
            else:
                right = mid - 1  # Target is in the left half

        return False  # Target not found


"""
The code is implemented within the searchMatrix function of the Solution class. Here's the breakdown:

First, we perform a quick check to handle edge cases. If the matrix is empty or any row is empty, we directly return False.

We retrieve the number of rows and columns of the matrix.

We initialize the left and right pointers for binary search. Since we treat the matrix as a 1D array, the left pointer is set to 0, and the right pointer is set to the last index of the matrix.

We enter the binary search loop, which continues until the left pointer becomes greater than the right pointer.

Inside the loop, we calculate the middle index mid using the formula (left + right) // 2. The element at the corresponding position in the matrix is retrieved using matrix[mid // cols][mid % cols], where mid // cols gives the row index, and mid % cols gives the column index.

We compare the retrieved element num with the target. If they are equal, we have found the target, and we return True.

If num is less than the target, it means the target is in the right half of the remaining search space. So, we update the left pointer to mid + 1.

If num is greater than the target, it means the target is in the left half of the remaining search space. So, we update the right pointer to mid - 1.

If the loop finishes without finding the target, we return False.

The code efficiently searches for the target in the matrix using binary search and returns True if found or False otherwise."""
