"""
Question Explanation:

You are given the head of a singly linked list. Your task is to reverse the list and return the head of the reversed list. The input linked list is represented by the class ListNode, where each node has a value (val) and a next pointer (next) to the next node in the list.

Follow-up:

The follow-up part of the question asks you to implement both iterative and recursive approaches to reverse the linked list.

Code Implementation:

We'll start by defining the ListNode class and the Solution class. The Solution class will contain two methods: reverseListIterative for the iterative solution and reverseListRecursive for the recursive solution. We'll add detailed comments for better understanding."""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseListIterative(self, head):
        # Base case: If the list is empty or has only one node, return the head itself
        if not head or not head.next:
            return head

        # Initialize three pointers: prev, curr, and nxt
        prev = None
        curr = head

        # Traverse the list, reversing the links of each node
        while curr:
            nxt = curr.next  # Store the next node
            curr.next = prev  # Reverse the link of the current node

            # Move prev and curr pointers one step forward
            prev = curr
            curr = nxt

        # Return the new head of the reversed list
        return prev

    def reverseListRecursive(self, head):
        # Base case: If the list is empty or has only one node, return the head itself
        if not head or not head.next:
            return head

        # Recursive call to reverse the rest of the list
        reversed_head = self.reverseListRecursive(head.next)

        # Reverse the link of the current node
        head.next.next = head
        head.next = None

        # Return the new head of the reversed list
        return reversed_head


"""
Explanation of the Code:

We define the ListNode class, representing a node in the singly linked list. Each node has a value (val) and a next pointer (next) pointing to the next node in the list.

We define the Solution class to contain our two methods for reversing the linked list.

The reverseListIterative method follows the iterative approach explained earlier in the previous response. It initializes three pointers prev, curr, and nxt, and then iteratively reverses the links of each node by updating the pointers.

The reverseListRecursive method follows the recursive approach. The base case checks if the list is empty or has only one node, in which case it returns the head itself (unchanged).

In the recursive approach, we call the reverseListRecursive function on the next node in the list (head.next) to reverse the rest of the list.

Once the recursive call returns, we have the new head of the reversed list. To reverse the link of the current node, we set the next pointer of the next node (head.next.next) to point back to the current node (head). Then, we set the next pointer of the current node (head.next) to None to break the link from the reversed part of the list.

Finally, the method returns the new head of the reversed list."""
