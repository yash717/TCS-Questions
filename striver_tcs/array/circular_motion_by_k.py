def reverse(arr, start, end):
    while start < end:
        arr[start], arr[end] = arr[end], arr[start]
        start += 1
        end -= 1


def rotate(arr, k):
    n = len(arr)
    k = k % n
    reverse(arr, 0, n-1)
    reverse(arr, 0, k-1)
    reverse(arr, k, n-1)


# Test cases
nums1 = [1, 2, 3, 4, 5, 6, 7]
k1 = 3
rotate(nums1, k1)
print("Example 1:")
print("Input:", nums1)

nums2 = [-1, -100, 3, 99]
k2 = 2
rotate(nums2, k2)
print("\nExample 2:")
print("Input:", nums2)
