
"""
The given code aims to merge two sorted arrays,
arr1 and arr2, in a different approach compared to the previous solution.
Although the goal is the same, the implementation differs. Let's go through each 
line of the code and provide an explanation with comments:

The code defines a function merge that takes two arrays arr1 and arr2,
along with their respective lengths n and m, as input.
It initializes two pointers, left and right, to keep track of the elements in arr1 and arr2, respectively.


The code uses a while loop to compare the elements of arr1 and arr2 and swaps them if necessary.
It continues swapping the elements until arr1[left] is smaller than or equal to arr2[right].
The pointers left and right are updated accordingly to move towards the center of the arrays.
The loop breaks when the condition is no longer satisfied.
"""


def merge(arr1, arr2, n, m):

    # Declare 2 pointers:
    left = n - 1
    right = 0

    # Swap the elements until arr1[left] is smaller than arr2[right]:
    while left >= 0 and right < m:
        if arr1[left] > arr2[right]:
            arr1[left], arr2[right] = arr2[right], arr1[left]
            left -= 1
            right += 1
        else:
            break

    # Sort arr1[] and arr2[] individually:
    arr1.sort()
    arr2.sort()


# MORE OPTIMIZED CODE


"""
The given problem asks us to merge two sorted integer arrays, nums1 and nums2, into a single sorted array. nums1 has enough space at the end to accommodate the merged elements.

To solve this problem, we can use a two-pointer approach. We'll start from the end of both arrays and compare the elements. We'll place the larger element at the end of nums1, and then move the pointer accordingly. We'll repeat this process until we have merged all the elements.

Here's a step-by-step explanation of the approach:

Initialize two pointers, p1 and p2, to point to the last non-zero element in nums1 and nums2, respectively.

Initialize a pointer p to point to the last position of nums1, which is m + n - 1.

While both p1 and p2 are greater than or equal to 0:

Compare nums1[p1] and nums2[p2].
If nums1[p1] is greater or equal, place it at position p in nums1 and decrement p1.
Otherwise, if nums2[p2] is greater, place it at position p in nums1 and decrement p2.
Decrement p to move to the next position.
If there are remaining elements in nums2, copy them to the beginning of nums1.

Here's the code that implements the above steps with detailed comments:"""


class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None
        """
        p1 = m - 1  # Pointer for nums1
        p2 = n - 1  # Pointer for nums2
        p = m + n - 1  # Pointer for merged array nums1

        # Compare elements from the end and place them in the merged array
        while p1 >= 0 and p2 >= 0:
            if nums1[p1] >= nums2[p2]:
                nums1[p] = nums1[p1]
                p1 -= 1
            else:
                nums1[p] = nums2[p2]
                p2 -= 1
            p -= 1

        # Copy remaining elements from nums2 to nums1
        nums1[:p2 + 1] = nums2[:p2 + 1]


# LEETCODE SOLUTION

class Solution(object):
    def merge(self, nums1, m, nums2, n):
        i = m-1
        j = n-1
        k = m+n-1
        while j >= 0:
            if i >= 0 and nums1[i] > nums2[j]:
                nums1[k] = nums1[i]
                i -= 1
            else:
                nums1[k] = nums2[j]
                j -= 1
            k -= 1
