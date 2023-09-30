class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        # Initialize two pointers, left and right, to track the current search range.
        left, right = 0, len(nums) - 1

        # Perform binary search as long as left is less than or equal to right.
        while left <= right:
            # Calculate the middle index using binary search.
            mid = left + (right - left) // 2

            # Check if the middle element is equal to the target.
            if nums[mid] == target:
                return mid

            # Check if the left half is sorted.
            if nums[left] <= nums[mid]:
                # Check if the target is within the sorted left half.
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            # If the left half is not sorted, the right half must be sorted.
            else:
                # Check if the target is within the sorted right half.
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1

        # If the target is not found, return -1.
        return -1
