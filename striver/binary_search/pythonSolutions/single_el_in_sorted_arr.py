class Solution(object):
    def singleNonDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Initialize two pointers, left and right, to track the current search range.
        left, right = 0, len(nums) - 1

        # Perform binary search as long as left is less than right.
        while left < right:
            # Calculate the middle index using binary search.
            mid = left + (right - left) // 2

            # Check if mid is an even index. If it's odd, make it even.
            if mid % 2 == 1:
                mid -= 1

            # Compare the element at mid with the element at the next index.
            # If they are different, the single element is on the left side.
            if nums[mid] != nums[mid + 1]:
                right = mid
            else:
                # If mid and the next element are the same, the single element is on the right side.
                left = mid + 2

        # Return the element at the left index, which is the single element.
        return nums[left]
