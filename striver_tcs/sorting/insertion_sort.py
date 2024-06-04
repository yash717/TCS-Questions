# Problem Statement: Given an array of N integers, write a program to implement the Insertion sorting algorithm.
#
# Examples:
#
# Example 1:
# Input: N = 6, array[] = [13,46,24,52,20,9]
# Output: 9,13,20,24,46,52
# Explanation:
# After sorting the array is: 9,13,20,24,46,52
#
# Example 2:
# Input: N=5, array[] = [5,4,3,2,1]
# Output: 1,2,3,4,5
# Explanation: After sorting the array is: 1,2,3,4,5

def insertion_sort(arr):
    """
    Function to perform Insertion Sort on the given array.

    Parameters:
        arr (list): The input array to be sorted.

    Returns:
        None (The input array is sorted in place).
    """
    # Insertion sort
    for i in range(len(arr)):
        j = i
        while j > 0 and arr[j - 1] > arr[j]:
            # Swap adjacent elements if they are out of order
            arr[j], arr[j - 1] = arr[j - 1], arr[j]
            j -= 1


# Test the function
array = [13, 46, 24, 52, 20, 9]
print("Before Insertion Sort:", array)
insertion_sort(array)
print("After Insertion Sort:", array)
