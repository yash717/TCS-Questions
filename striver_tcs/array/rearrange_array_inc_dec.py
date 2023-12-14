def rearrange(arr):
    arr.sort()
    mid = len(arr)//2

    arr[mid:] = arr[mid:][::-1]
    return arr


# Test cases
arr1 = [8, 7, 1, 6, 5, 9]
arr2 = [4, 2, 8, 6, 15, 5, 9, 20]

result1 = rearrange(arr1)
result2 = rearrange(arr2)

# Displaying the results
print("Example 1:")
print(result1)

print("\nExample 2:")
print(result2)
