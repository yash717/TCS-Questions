"""
Given an integer array nums, the task is to find the number of reverse pairs in the array. A reverse pair is defined as a pair (i, j) where 0 <= i < j < nums.length and nums[i] > 2 * nums[j].

To solve this problem, we will provide two solutions: a brute force solution and an optimized solution.

Brute Force Solution:
The brute force solution involves comparing each element in the array with all subsequent elements to check if it forms a reverse pair. We can iterate over the array and for each element nums[i], iterate over all elements nums[j] where j > i. If nums[i] > 2 * nums[j], we increment a count variable to keep track of the reverse pairs.

Here's the code for the brute force solution with detailed comments


"""
class Solution(object):
    def reversePairs(self, nums):
        count = 0
        n = len(nums)
        
        for i in range(n):
            for j in range(i + 1, n):
                if nums[i] > 2 * nums[j]:
                    count += 1
        
        return count

"""
Optimized Solution:
The optimized solution makes use of the merge sort algorithm to efficiently count the reverse pairs. The idea is to divide the array into two halves, recursively count the reverse pairs in each half, and then merge the two sorted halves while counting additional reverse pairs.

Here's the code for the optimized solution with detailed comments:"""

class Solution(object):
    def reversePairs(self, nums):
        def mergeSort(nums, start, end):
            if start >= end:
                return 0
            
            mid = (start + end) // 2
            count = mergeSort(nums, start, mid) + mergeSort(nums, mid + 1, end)
            
            j = mid + 1
            for i in range(start, mid + 1):
                while j <= end and nums[i] > 2 * nums[j]:
                    j += 1
                count += j - (mid + 1)
            
            nums[start:end+1] = sorted(nums[start:end+1])
            
            return count
        
        return mergeSort(nums, 0, len(nums) - 1)
