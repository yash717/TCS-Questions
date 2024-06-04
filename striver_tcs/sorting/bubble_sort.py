# Problem Statement: Given an array of N integers, write a program to implement the Bubble Sorting algorithm.
#
# Examples:
#
# Example 1:
# Input: N = 6, array[] = [13,46,24,52,20,9]
# Output: 9,13,20,24,46,52
# Explanation: After sorting we get 9,13,20,24,46,52
#
# Input: N = 5, array[] = [5,4,3,2,1]
# Output: 1,2,3,4,5
# Explanation: After sorting we get 1,2,3,4,5

def bubble_sort(arr):
    """
    Function to perform Bubble Sort on the given array.

    Parameters:
        arr (list): The input array to be sorted.

    Returns:
        None (The input array is sorted in place).
    """
    # bubble sort
    for i in range(len(arr) - 1, 0, -1):
        did_swap = False  # Flag to track if any swap occurred during the iteration
        for j in range(i):
            if arr[j] > arr[j + 1]:  # Compare adjacent elements
                # Swap if they are in the wrong order
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                did_swap = True  # Set the flag to True if a swap occurs
        # If no swap occurred in this iteration, the array is already sorted
        if not did_swap:
            break


# Test the function
array = [13, 46, 24, 52, 20, 9]
print("Before Using Bubble Sort:", array)
bubble_sort(array)
print("After Using Bubble Sort:", array)
