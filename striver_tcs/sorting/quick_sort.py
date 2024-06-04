def partition(arr, low, high):
    """
    Partition the array based on the pivot element.

    Parameters:
        arr (list): The input array.
        low (int): Starting index of the partition.
        high (int): Ending index of the partition.

    Returns:
        int: The partition index.
    """
    pivot = arr[low]  # Choosing the pivot element (first element in this implementation)
    i = low
    j = high

    while True:
        while arr[i] <= pivot and i <= high:  # Find the first element greater than pivot
            i += 1
        while arr[j] > pivot and j >= low:  # Find the first element smaller than pivot
            j -= 1
        if i < j:
            arr[i], arr[j] = arr[j], arr[i]  # Swap elements
        else:
            break

    arr[low], arr[j] = arr[j], arr[low]  # Swap pivot with the element at j
    return j  # Return partition index


def quick_sort(arr, low, high):
    """
    Sort the array using Quick Sort algorithm.

    Parameters:
        arr (list): The input array.
        low (int): Starting index of the partition.
        high (int): Ending index of the partition.

    Returns:
        None (The array is sorted in place).
    """
    if low < high:
        p_index = partition(arr, low, high)  # Get partition index
        quick_sort(arr, low, p_index - 1)  # Sort left subarray
        quick_sort(arr, p_index + 1, high)  # Sort right subarray


# Test the function
arr = [4, 6, 2, 5, 7, 9, 1, 3]
print("Before Quick Sort:", arr)
quick_sort(arr, 0, len(arr) - 1)
print("After Quick Sort:", arr)
