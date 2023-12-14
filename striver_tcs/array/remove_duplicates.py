def removeduplicates(nums):
    if not nums:
        return 0

    k = 0

    for j in range(1, len(nums)):
        if nums[j] != nums[k]:
            k += 1
            nums[k] = nums[j]
    return k+1


# Example 1
arr1 = [1, 1, 2]
result1 = removeduplicates(arr1)
print("Example 1:")
print("Output Array:", arr1[:result1])  # Displaying the unique elements

# Example 2
arr2 = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
result2 = removeduplicates(arr2)
print("\nExample 2:")
print("Output Array:", arr2[:result2])  # Displaying the unique elements
