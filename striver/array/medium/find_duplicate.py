from typing import List


def findDuplicate(nums: List[int]) -> int:
    # Step 1: Initialize the slow and fast pointers to the first element of the array
    slow = nums[0]
    fast = nums[0]

    # Step 2: Find the intersection point of the two pointers
    while True:
        # Move the slow pointer one step at a time
        slow = nums[slow]
        # Move the fast pointer two steps at a time
        fast = nums[nums[fast]]

        # Check if the pointers have met at the same position
        if slow == fast:
            break

    # Step 3: Move one pointer to the start and keep the other pointer at the intersection point
    fast = nums[0]
    while slow != fast:
        # Move both pointers one step at a time until they meet again
        slow = nums[slow]
        fast = nums[fast]

    # Step 4: Return the duplicate number
    return slow


"""
The code defines a function findDuplicate that takes an input array nums and returns the duplicate number.
Two pointers, slow and fast, are initialized to the first element of the array.

The code uses the concept of Floyd's Tortoise and Hare algorithm to find the intersection point of the two pointers.
The slow pointer moves one step at a time, while the fast pointer moves two steps at a time.
If there is a cycle in the array, the two pointers will eventually meet at the intersection point.
This indicates the presence of a duplicate number in the array.

After finding the intersection point, one pointer (fast) is reset to the first element of the array.
The other pointer (slow) remains at the intersection point.
Both pointers move one step at a time until they meet again.
The meeting point will be the duplicate number in the array.

The duplicate number is returned as the output of the function.



"""
