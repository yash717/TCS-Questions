# brute force
def second_smallest(arr, n):
    arr.sort()
    print(arr[1])


# optimal
def second_smallest_2(arr, n):
    pass


# brute force
def second_largest(arr, n):
    arr.sort()
    print(arr[n-2])


arr = [1, 2, 4, 7, 7, 5]
n = 6
second_largest(arr, n)
second_smallest_2(arr, n)
