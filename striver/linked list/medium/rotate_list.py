"""
Problem Statement:
Given the head of a singly linked list and an integer 'k', you need to rotate the list to the right by 'k' places.

For example:

Input: head = [1,2,3,4,5], k = 2
Output: [4,5,1,2,3]

Input: head = [0,1,2], k = 4
Output: [2,0,1]

Explanation of the example:
In the first example, we have a linked list with values [1,2,3,4,5]. If we rotate the list to the right by 2 places, the new list becomes [4,5,1,2,3].

In the second example, we have a linked list with values [0,1,2]. If we rotate the list to the right by 4 places, the new list becomes [2,0,1].

Now, let's discuss the brute force approach and the optimal solution:

Brute Force Approach:
To perform a right rotation, we can traverse the linked list 'k' times, and in each iteration, we move the last node to the front of the list. We can repeat this process 'k' times to achieve the final rotated list. The time complexity of this approach will be O(k*n), where 'n' is the number of nodes in the linked list.

Optimal Solution:
The brute force approach can be optimized using a two-pointer technique. First, we need to find the length of the linked list. Then, we calculate the new position of the head after rotation. To find the new position, we use the following formula: new_head_position = (length - k) % length. Once we have the new head position, we update the pointers to achieve the rotation.

The time complexity of this optimal solution is O(n), where 'n' is the number of nodes in the linked list.

Now, let's write the code for the optimal solution with detailed comments:"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution(object):
    def rotateRight(self, head, k):
        # Edge case: If the linked list is empty or has only one node, return the head as it is.
        if not head or not head.next:
            return head

        # Step 1: Calculate the length of the linked list
        length = 1
        current = head
        while current.next:
            current = current.next
            length += 1

        # Step 2: Calculate the new position of the head after rotation
        new_head_position = (length - k) % length

        # If the new position is the same as the current head position, no rotation is needed
        if new_head_position == 0:
            return head

        # Step 3: Find the new head and tail of the rotated linked list
        current = head
        for _ in range(new_head_position - 1):
            current = current.next
        new_head = current.next
        current.next = None

        # Step 4: Update the pointers to achieve the rotation
        tail = new_head
        while tail.next:
            tail = tail.next
        tail.next = head

        # Step 5: Return the new head of the rotated linked list
        return new_head


"""
DRY RUN


Sure, let's do a dry run of the optimal solution with an example:

Example:
Input: head = [1,2,3,4,5], k = 2

Steps:

Calculate the length of the linked list.

The linked list is [1,2,3,4,5].
Length = 5
Calculate the new position of the head after rotation.

new_head_position = (5 - 2) % 5 = 3
Find the new head and tail of the rotated linked list.

current = head (1)
Move current 2 steps (new_head_position - 1) to reach the node before the new head (current = 3)
new_head = current.next (new_head = 3.next = 4)
current.next = None (Set the next of current to None)
Update the pointers to achieve the rotation.

The linked list after the first rotation:
4 -> 5 -> 1 -> 2 -> 3 (new_head -> 4 -> 5 -> 1 -> 2 -> 3 -> None)
Find the tail of the rotated linked list (tail = 3)
Connect the tail of the rotated linked list to the original head.

The linked list after the second rotation:
4 -> 5 -> 1 -> 2 -> 3 -> 1 -> 2 -> 3 (new_head -> 4 -> 5 -> 1 -> 2 -> 3 -> 1 -> 2 -> 3 -> None)
Return the new head of the rotated linked list (new_head = 4).

Final Output:
4 -> 5 -> 1 -> 2 -> 3 (new_head -> 4 -> 5 -> 1 -> 2 -> 3 -> None)

The linked list is rotated to the right by 2 places, and the new head is 4."""


"""
ANOTHER DRY RUN TEST


Example:
Linked list: 4 -> 5 -> 1 -> 2 -> 3 (new_head -> 4 -> 5 -> 1 -> 2 -> 3 -> None)

Initially, the "tail" pointer is pointing to the "new_head" node, which is 4. Now we traverse the linked list until the "tail" reaches the last node, which is 3.

Step 1:
tail = 4 (new_head)

Step 2:
tail = tail.next => tail = 4.next => tail = 5

Step 3:
tail = tail.next => tail = 5.next => tail = 1

Step 4:
tail = tail.next => tail = 1.next => tail = 2

Step 5:
tail = tail.next => tail = 2.next => tail = 3

Step 6:
tail = tail.next => tail = 3.next => tail = None (since 3 is the last node)

Now, the "tail" pointer has reached the end of the linked list, and it is pointing to the last node, which is 3.

Step 7:
tail.next = head => 3.next = 4 (original head)

After this step, the linked list becomes a circular linked list with the last node (3) pointing to the original head (4).

Final Result:
Linked list: 4 -> 5 -> 1 -> 2 -> 3 -> 4 (new_head -> 4 -> 5 -> 1 -> 2 -> 3 -> 4 -> None)

The linked list is now rotated to the right by 2 places, and the rotation is achieved by connecting the tail of the rotated list (last node) to the original head."""
