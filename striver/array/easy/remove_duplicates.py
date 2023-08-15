"""
Sure, let's approach this problem step by step.

Brute Force Solution:
The brute force solution for removing duplicates from a sorted array is straightforward. We can use two pointers: one to keep track of the current element and another to traverse the array and remove any duplicates.
Here's how the brute force approach works:

Initialize two pointers i and j, where i points to the first element of the array, and j starts from the second element.
Compare nums[i] with nums[j]. If they are equal, it means we have a duplicate.
Shift all the elements to the right of j by one position to remove the duplicate.
Update the length of the array (n) to remove the duplicate element.
Continue this process until j reaches the end of the array.
The time complexity of this approach is O(n^2) because in the worst case, we may have to shift all the elements to the right for each duplicate element.

Optimal Solution:
The given array is already sorted in non-decreasing order, so we can use a more efficient approach to remove duplicates.
Here's how the optimal approach works:

Initialize two pointers i and j, where i points to the first element of the array, and j starts from the second element.
Compare nums[i] with nums[j]. If they are not equal, it means we have found a unique element.
Increment i by 1 and assign nums[j] to nums[i] to keep track of the unique elements.
Continue this process until j reaches the end of the array.
The time complexity of this approach is O(n), where n is the number of elements in the array. This is because we only traverse the array once to find and remove duplicates.

Let's write the code for the optimal solution with detailed comments:"""


class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Check if the array is empty
        if not nums:
            return 0

        # Initialize the first pointer 'i' to keep track of unique elements
        i = 0

        # Start the second pointer 'j' from the second element
        for j in range(1, len(nums)):
            # Compare 'nums[i]' with 'nums[j]'
            if nums[i] != nums[j]:
                # If 'nums[i]' and 'nums[j]' are different, it means we found a unique element
                # Increment 'i' by 1 and update 'nums[i]' to 'nums[j]' to store the unique element
                i += 1
                nums[i] = nums[j]

        # Return the number of unique elements (index 'i' + 1)
        return i + 1


"""

This optimal solution will efficiently remove duplicates from the sorted array in-place and maintain the relative order of the elements. The returned value k represents the number of unique elements in the array, and the modified array contains the first k unique elements, with the remaining elements being ignored.





"""
