def median(matrix: [[int]], m: int, n: int) -> int:
    # Define a function to count elements less than or equal to a given value.
    def count_elements_less_equal(mid_val):
        count = 0
        for row in matrix:
            count += sum(1 for num in row if num <= mid_val)
        return count

    # Find the minimum value in the entire matrix.
    min_val = min(min(row) for row in matrix)
    
    # Find the maximum value in the entire matrix.
    max_val = max(max(row) for row in matrix)

    # Calculate the desired position of the median in the sorted list of elements.
    desired_count = (m * n + 1) // 2

    # Perform binary search to find the median.
    while min_val < max_val:
        # Calculate the middle value of the current search range.
        mid_val = (min_val + max_val) // 2

        # Count the number of elements less than or equal to mid_val in the matrix.
        count = count_elements_less_equal(mid_val)

        # Adjust the search range based on the count of elements.
        if count < desired_count:
            min_val = mid_val + 1
        else:
            max_val = mid_val

    # Return the minimum value of the search range as the median.
    return min_val
