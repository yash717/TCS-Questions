'''This function takes two parameters: permutation, which is the input array of integers
and n, which is the length of the array. It returns the next permutation of the input array.

The algorithm follows these steps:

Find the first index from the right where the element is smaller than the next element.
This step identifies the "pivot" element.
If no pivot is found, it means the array is already in the highest lexicographical order.
In this case, we sort the array in ascending order and return it.
Find the first index from the right where the element is greater than the pivot element.
Swap the pivot element with the element found in step 3.
Reverse the subarray from index i+1 to the end of the array.
By following these steps, we can find the next lexicographically greater permutation of the input array in-place.'''


'''coding ninja code'''


def nextPermutation(permutation, n):
    # Step 1: Find the first index from the right where the element is smaller than the next element
    i = n - 2
    while i >= 0 and permutation[i] >= permutation[i+1]:
        i -= 1

    # Step 2: If no such index is found, the array is already in the highest lexicographical order
    if i == -1:
        permutation.sort()  # Sort the array in ascending order
        return permutation

    # Step 3: Find the first index from the right where the element is greater than the element found in step 1
    j = n - 1
    while permutation[j] <= permutation[i]:
        j -= 1

    # Step 4: Swap the elements at indices i and j
    permutation[i], permutation[j] = permutation[j], permutation[i]

    # Step 5: Reverse the subarray from i+1 to the end of the array
    left = i + 1
    right = n - 1
    while left < right:
        permutation[left], permutation[right] = permutation[right], permutation[left]
        left += 1
        right -= 1

    return permutation


'''leetcode code'''


class Solution(object):
    def nextPermutation(self, nums):
        # Find the first decreasing element from the right
        i = len(nums) - 2
        while i >= 0 and nums[i] >= nums[i + 1]:
            i -= 1

        if i >= 0:
            # Find the smallest element greater than the decreasing element
            j = len(nums) - 1
            while j > i and nums[j] <= nums[i]:
                j -= 1
            # Swap the decreasing element with the smallest greater element
            nums[i], nums[j] = nums[j], nums[i]

        # Reverse the remaining part after the decreasing element
        left = i + 1
        right = len(nums) - 1
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1
