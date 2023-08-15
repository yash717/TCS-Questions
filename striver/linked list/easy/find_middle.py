"""
Question Explanation:

You are given the head of a singly linked list. Your task is to find and return the middle node(s) of the linked list. If the list has an odd number of nodes, there will be one middle node. If the list has an even number of nodes, there will be two middle nodes, and you should return the second middle node.

Code Implementation:

To solve this problem, we'll use the slow and fast pointer approach. The slow pointer moves one step at a time, while the fast pointer moves two steps at a time. When the fast pointer reaches the end of the list, the slow pointer will be at the middle node(s)."""

# Definition for singly-linked list.


class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def middleNode(self, head):
        # Initialize slow and fast pointers to the head of the list
        slow = head
        fast = head

        # Traverse the list using slow and fast pointers
        while fast and fast.next:
            slow = slow.next  # Move slow pointer one step
            fast = fast.next.next  # Move fast pointer two steps

        # When the fast pointer reaches the end, the slow pointer will be at the middle node(s)
        return slow


"""
Explanation of the Code:

We define the ListNode class, representing a node in the singly linked list. Each node has a value (val) and a next pointer (next) pointing to the next node in the list.

We define the Solution class, which contains the method middleNode.

In the middleNode method, we initialize two pointers: slow and fast. Both pointers are set to the head of the linked list initially.

We use a while loop to traverse the list using the slow and fast pointers. The loop continues as long as the fast pointer (fast) and its next node (fast.next) are not None.

In each iteration of the loop, the slow pointer (slow) moves one step forward (slow = slow.next), and the fast pointer (fast) moves two steps forward (fast = fast.next.next).

When the loop ends, it means the fast pointer has reached the end of the list (i.e., fast or fast.next is None). At this point, the slow pointer will be at the middle node(s) of the list.

Finally, we return the slow pointer, which points to the middle node(s)."""
