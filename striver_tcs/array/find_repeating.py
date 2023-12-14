def findRepeating(nums):
    seen = set()
    repeating = set()

    for i in nums:
        if i in seen:
            repeating.add(i)
        else:
            seen.add(i)

    return list(repeating)


# Example 1
arr1 = [1, 1, 2, 3, 4, 4, 5, 2]
result1 = findRepeating(arr1)
print("Example 1:")
print("Output:", result1)

# Example 2
arr2 = [1, 1, 0]
result2 = findRepeating(arr2)
print("\nExample 2:")
print("Output:", result2)
