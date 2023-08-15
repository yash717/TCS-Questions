from os import *
from sys import *
from collections import *
from math import *


def merge(arr1, low, mid, high):
    left = low
    right = mid + 1
    temp = []
    cnt = 0

    while left <= mid and right <= high:
        if arr1[left] <= arr1[right]:
            temp.append(arr1[left])
            left += 1
        else:
            temp.append(arr1[right])
            right += 1
            cnt += mid - left + 1

    while left <= mid:
        temp.append(arr1[left])
        left += 1

    while right <= high:
        temp.append(arr1[right])
        right += 1

    for i in range(low, high + 1):
        arr1[i] = temp[i - low]

    return cnt


def mergeSort(arr1, low, high):
    cnt = 0
    if low >= high:
        return cnt
    mid = (low + high) // 2
    cnt += mergeSort(arr1, low, mid)
    cnt += mergeSort(arr1, mid + 1, high)
    cnt += merge(arr1, low, mid, high)
    return cnt


def getInversions(arr, n):
    return mergeSort(arr, 0, n - 1)


def takeInput():
    n = int(input())
    arr = list(map(int, input().strip().split()))
    return arr, n


arr, n = takeInput()
print(getInversions(arr, n))


"""
This is the merge function that takes an array arr, the lower index low,
the middle index mid, and the higher index high as parameters.
It initializes an empty list temp to store the sorted elements during the merging process.
It initializes the left and right pointers to the starting indices of the left and right halves of the array,
respectively.
It initializes the cnt variable to count the number of pairs.
"""


"""
This loop compares elements from the left and right halves of the array.
If the element at arr[left] is less than or equal to the element at arr[right],
it appends arr[left] to the temp list and moves the left pointer to the next element.
If the element at arr[left] is greater than the element at arr[right],
it appends arr[right] to the temp list, increments the cnt variable by (mid - left + 1)
(to count the inversions), and moves the right pointer to the next element.
"""

"""
This loop appends the remaining elements from the left half of the array to the temp list.
"""


"""

This loop appends the remaining elements from the right half of the array to the temp list.

"""

"""

This loop transfers all the elements from the temp list back to the original arr array.
"""
"""



he merge function returns the cnt variable, which represents the count of inversions in the current merge.
"""
"""


This is the mergeSort function that performs the merge sort algorithm.
It takes the arr array, the lower index low, and the higher index high as parameters.
It initializes the cnt variable to count the inversions.
If low is greater than or equal to high, the function returns cnt (base case).
It calculates the mid index as the floor division of (low + high) / 2.
It recursively calls mergeSort on the left half (low to mid), the right half (mid + 1 to high),
and then merges the sorted halves using the merge function.
It accumulates the inversion count by adding the counts returned from the recursive calls.
"""
"""



This is the numberOfInversions function that calculates the total number of inversions in the input array a.
It takes the array a and the size of the array n as parameters.
It assigns n as the length of the array (this line is not necessary as n is already passed as a parameter).
It calls the mergeSort function to perform the merge sort and returns the inversion count.
The overall code implements the merge sort algorithm with modifications to count the number of
inversions during the merging process. It uses the divide-and-conquer approach to sort the array
and count the inversions efficiently.
"""
