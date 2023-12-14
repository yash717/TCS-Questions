# brute force

def reverseArray(arr, n):
    for i in arr[::-1]:
        print(i)


# Using an extra array.

def reverseArray2(arr, n):
    ans = [0]*n
    for i in range(n-1, -1, -1):
        ans[n-i-1] = arr[i]
    printArray(arr, n)

# Space-optimized iterative method


def reverseArray3(arr, n):
    pointer1 = 0
    pointer2 = n-1
    while pointer1 < pointer2:
        arr[pointer1], arr[pointer2] = arr[pointer2], arr[pointer1]
        pointer1 += 1
        pointer2 -= 1
    printArray(arr, n)


# new approach

def reverseArray4(arr, n):
    arr.reverse()
    for i in range(n):
        print(arr[i], end=" ")

# function to print array


def printArray(arr, n):
    for i in range(n):
        print(arr[i], end=" ")
    print()


# Driver Code
arr = [5, 4, 3, 2, 1]
n = len(arr)
reverseArray4(arr, n)
