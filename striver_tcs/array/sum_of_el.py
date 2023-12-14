def summation(arr):
    total_sum = 0
    for i in arr:
        total_sum += i

    return total_sum


# Test cases
arr1 = [1, 2, 3, 4, 5]
arr2 = [1, 2, 1, 1, 5, 1]

result1 = summation(arr1)
result2 = summation(arr2)

# Displaying the results
print("Example 1:")
print("Output:", result1)

print("\nExample 2:")
print("Output:", result2)
