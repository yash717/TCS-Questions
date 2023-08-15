
class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


def removeKthNode(head, k):
    dummy = Node()
    dummy.next = head

    slow = dummy
    fast = dummy

    for i in range(1, k+1):
        fast = fast.next

    while fast.next != None:
        slow = slow.next
        fast = fast.next

    slow.next = slow.next.next

    return dummy.next
# leetcode

# Definition for singly-linked list.


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def removeNthFromEnd(head, n):
    # Step 1: Create a new node called 'start' and set its 'next' pointer to the 'head' of the linked list.
    start = ListNode()
    start.next = head

    # Step 2: Initialize 'fast' and 'slow' pointers, both pointing to the 'start' node.
    fast = start
    slow = start

    # Step 3: Move the 'fast' pointer 'n' steps ahead initially.
    for i in range(1, n + 1):
        fast = fast.next

    # Step 4: Move both 'fast' and 'slow' pointers until 'fast' reaches the last node (None).
    while fast.next is not None:
        fast = fast.next
        slow = slow.next

    # Step 5: At this point, 'slow' points to the (sz - n - 1)th node from the beginning.
    # Adjust the pointers to remove the nth node from the end.
    slow.next = slow.next.next

    # Step 6: Return the head of the modified list (next node after the 'start' node).
    return start.next


"""

Detailed Explanation:

We start by defining the ListNode class that represents a node in the singly linked list. Each node has a val attribute to store the node's value and a next pointer to point to the next node in the list.

The removeNthFromEnd function takes two parameters: head (the head of the linked list) and n (the position of the node to be removed from the end).

We create a new node called start and set its next pointer to the head of the linked list. This dummy node helps us handle the edge case when we need to remove the first node.

Two pointers fast and slow are initialized, both pointing to the start node. These pointers will be used to traverse the linked list.

The fast pointer is moved n steps ahead initially using a loop that runs from 1 to n+1. This ensures that the distance between fast and slow is n.

The first loop ends, and now the fast pointer is n nodes ahead of the slow pointer.

The second loop is used to move both fast and slow pointers until fast reaches the last node (None). At this point, slow will be pointing to the (sz - n - 1)th node from the beginning.

We adjust the pointers to remove the nth node from the end by setting the next pointer of the (sz - n - 1)th node to skip the nth node.

Finally, the start.next is returned, which is the head of the modified list.

The implementation uses the dummy node (start) to handle edge cases, and it follows the optimal approach to remove the nth node from the end of the linked list in a single pass. The code ensures a time complexity of O(sz) and a space complexity of O(1)."""
