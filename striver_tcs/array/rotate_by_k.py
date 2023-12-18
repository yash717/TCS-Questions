def reverseArray(arr, start, end):
    # Helper function to reverse elements in the array from start to end indices
    while start < end:
        arr[start], arr[end] = arr[end], arr[start]
        start += 1
        end -= 1


def rotateArray(arr, k, direction):
    n = len(arr)
    k %= n  # Normalize k in case it's greater than array length

    if direction == 'right':
        # Rotate the array to the right by k elements
        reverseArray(arr, 0, n - 1)        # Reverse the entire array
        reverseArray(arr, 0, k - 1)       # Reverse the first k elements
        reverseArray(arr, k, n - 1)       # Reverse the remaining elements

    elif direction == 'left':
        # Rotate the array to the left by k elements
        reverseArray(arr, 0, n - 1)       # Reverse the entire array
        reverseArray(arr, 0, n - k - 1)   # Reverse the first n - k elements
        reverseArray(arr, n - k, n - 1)   # Reverse the remaining elements

    return arr


# Test cases
arr1 = [1, 2, 3, 4, 5, 6, 7]
k1 = 2
direction1 = 'right'
result1 = rotateArray(arr1, k1, direction1)
print("Example 1:")
print("Input:", arr1)
print("Output:", result1)

arr2 = [3, 7, 8, 9, 10, 11]
k2 = 3
direction2 = 'left'
result2 = rotateArray(arr2, k2, direction2)
print("\nExample 2:")
print("Input:", arr2)
print("Output:", result2)
