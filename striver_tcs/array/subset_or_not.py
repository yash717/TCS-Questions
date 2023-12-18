def isSubset(arr1, arr2):
    # Sort both arrays for easier comparison
    arr1.sort()
    arr2.sort()

    # Initialize pointers for both arrays
    i, j = 0, 0

    # Iterate through both arrays
    while i < len(arr1) and j < len(arr2):
        # If elements at current positions match, move both pointers forward
        if arr1[i] == arr2[j]:
            i += 1
            j += 1
        # If the element in arr1 is smaller than the element in arr2
        elif arr1[i] < arr2[j]:
            return False  # Not a subset; element in arr1 missing in arr2
        else:
            j += 1  # Move arr2 pointer if element in arr1 is larger

    # Check if all elements from arr1 were found in arr2
    return i == len(arr1)


# Test cases
arr1_1 = [1, 3, 4, 5, 2]
arr2_1 = [2, 4, 3, 1, 7, 5, 15]
print("Output for Example 1:", "arr1[] is a subset of arr2[]" if isSubset(
    arr1_1, arr2_1) else "arr1[] is not a subset of arr2[]")

arr1_2 = [1, 3, 4, 5, 2]
arr2_2 = [4, 5, 2]
print("Output for Example 2:", "arr1[] is a subset of arr2[]" if isSubset(
    arr1_2, arr2_2) else "arr1[] is not a subset of arr2[]")

arr1_3 = [1, 3, 4, 5, 2]
arr2_3 = [11, 12, 13, 15, 16]
print("Output for Example 3:", "arr1[] is a subset of arr2[]" if isSubset(
    arr1_3, arr2_3) else "arr1[] is not a subset of arr2[]")
