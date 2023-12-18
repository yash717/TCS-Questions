def searchElement(arr, k):
    # Traverse through the array elements
    for i in range(len(arr)):
        # Check if the current element matches the target value (k)
        if arr[i] == k:
            return i  # Return the index if the element is found

    return -1  # Return -1 if the element is not found


# Test cases
arr1 = [1, 2, 3, 4, 5]
k1 = 3
result1 = searchElement(arr1, k1)
print("Output for Example 1:", result1)

arr2 = [6, 7, 9, 5, 3, 10]
k2 = 10
result2 = searchElement(arr2, k2)
print("Output for Example 2:", result2)
