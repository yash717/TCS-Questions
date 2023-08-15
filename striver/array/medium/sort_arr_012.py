"""
The given problem asks us to sort an array nums containing integers representing colors,
specifically red (0), white (1), and blue (2).
We need to rearrange the elements of the array in place so that objects 
of the same color are adjacent and appear in the order red, white, and blue.

To solve this problem, we can use the Dutch National Flag Algorithm,
also known as the 3-way partitioning algorithm. This algorithm is efficient and works in a single pass through the array.

The steps of the Dutch National Flag Algorithm are as follows:

Initialize three pointers: low, mid, and high.

low points to the leftmost boundary of white (1) elements.
mid starts at the leftmost index and iterates through the array.
high points to the rightmost boundary of blue (2) elements.
Iterate through the array from mid to high:

If nums[mid] is 0, swap nums[mid] with nums[low] and increment both mid and low.
If nums[mid] is 1, increment mid only since it is already in the correct position.
If nums[mid] is 2, swap nums[mid] with nums[high] and decrement high.
After the iteration, the array will be sorted in place with the desired order of colors.

Here's the code that implements the above steps with detailed comments:"""


class Solution(object):
    def sortColors(self, nums):
        # Step 1: Initialize pointers
        low = 0
        mid = 0
        high = len(nums) - 1

        # Step 2: Iterate through the array
        while mid <= high:
            if nums[mid] == 0:
                # Swap nums[mid] with nums[low]
                nums[mid], nums[low] = nums[low], nums[mid]
                mid += 1
                low += 1
            elif nums[mid] == 1:
                # Increment mid since it is already in the correct position
                mid += 1
            else:
                # Swap nums[mid] with nums[high]
                nums[mid], nums[high] = nums[high], nums[mid]
                high -= 1

        # No need for explicit return as the array is modified in place


"""
This code defines a class Solution with a method sortColors that takes an array nums as input. 
It follows the steps described above to sort the array in place.

Note: The code assumes that nums contains integers representing the colors (0, 1, or 2) and the length of nums
is within the given constraints."""
