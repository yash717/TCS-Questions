def median(arr):
    arr.sort()
    n = len(arr)
    if n % 2 != 0:
        median = arr[(n)//2]
    else:
        median = (arr[n//2-1]+arr[n//2])/2
    return median


# Example 1
arr1 = [2, 4, 1, 3, 5]
result1 = median(arr1)
print("Example 1:")
print("Output:", result1)

# Example 2
arr2 = [2, 5, 1, 7]
result2 = median(arr2)
print("\nExample 2:")
print("Output:", result2)
