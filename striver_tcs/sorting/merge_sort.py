def merge(arr, low, mid, high):
    """
    Merge two sorted subarrays into one sorted array.

    Parameters:
        arr (list): The input array.
        low (int): Starting index of the first subarray.
        mid (int): Ending index of the first subarray.
        high (int): Ending index of the second subarray.

    Returns:
        None (The array is sorted in place).
    """
    temp = []  # Temporary array to store merged elements
    left = low  # Starting index of the first subarray
    right = mid + 1  # Starting index of the second subarray

    # Merge the two subarrays into temp
    while left <= mid and right <= high:
        if arr[left] <= arr[right]:
            temp.append(arr[left])
            left += 1
        else:
            temp.append(arr[right])
            right += 1

    # Copy remaining elements from the first subarray
    while left <= mid:
        temp.append(arr[left])
        left += 1

    # Copy remaining elements from the second subarray
    while right <= high:
        temp.append(arr[right])
        right += 1

    # Copy elements from temp back to arr
    for i in range(low, high + 1):
        arr[i] = temp[i - low]


def merge_sort(arr, low, high):
    """
    Sort the array using Merge Sort algorithm.

    Parameters:
        arr (list): The input array.
        low (int): Starting index of the array.
        high (int): Ending index of the array.

    Returns:
        None (The array is sorted in place).
    """
    if low < high:
        mid = (low + high) // 2  # Calculate the middle index
        merge_sort(arr, low, mid)  # Sort the left half
        merge_sort(arr, mid + 1, high)  # Sort the right half
        merge(arr, low, mid, high)  # Merge the sorted halves


# Test the function
arr1 = [4, 2, 1, 6, 7]
print("Before Merge Sort:", arr1)
merge_sort(arr1, 0, len(arr1) - 1)
print("After Merge Sort:", arr1)

arr2 = [3, 2, 8, 5, 1, 4, 23]
print("Before Merge Sort:", arr2)
merge_sort(arr2, 0, len(arr2) - 1)
print("After Merge Sort:", arr2)
