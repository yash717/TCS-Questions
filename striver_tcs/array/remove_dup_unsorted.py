def removeDuplicate(nums):
    seen = {}
    result = []

    for i in nums:
        if i not in seen:
            seen[i] = True
            result.append(i)

    return result


    # Example 1
arr1 = [2, 3, 1, 9, 3, 1, 3, 9]
result1 = removeDuplicate(arr1)
print("Example 1:")
print("Output Array:", result1)

# Example 2
arr2 = [4, 3, 9, 2, 4, 1, 10, 89, 34]
result2 = removeDuplicate(arr2)
print("\nExample 2:")
print("Output Array:", result2)
