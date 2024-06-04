# Problem Statement: Given an array of N integers, write a program to implement the Selection sorting algorithm.
#
# Examples:
#
# Example 1:
# Input: N = 6, array[] = [13,46,24,52,20,9]
# Output: 9,13,20,24,46,52
# Explanation: After sorting the array is: 9, 13, 20, 24, 46, 52
#
# Example 2:
# Input: N=5, array[] = [5,4,3,2,1]
# Output: 1,2,3,4,5
# Explanation: After sorting the array is: 1, 2, 3, 4, 5

def selection_sort(arr):
    """
    Function to perform Selection Sort on the given array.

    Parameters:
        arr (list): The input array to be sorted.

    Returns:
        None (The input array is sorted in place).
    """
    # Selection sort
    for i in range(len(arr) - 1):
        # Find the index of the minimum element in the unsorted part of the array
        min_index = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_index]:
                min_index = j
        # Swap the minimum element with the first element of the unsorted part
        arr[i], arr[min_index] = arr[min_index], arr[i]


# Test the function
array = [13, 46, 24, 52, 20, 9]
print("Before Selection Sort:", array)
selection_sort(array)
print("After Selection Sort:", array)
