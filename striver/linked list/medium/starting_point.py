"""
Brute Force Approach:

The brute force approach to find the starting node of the cycle is to use a hash set to keep track of the nodes that have been visited. We traverse the linked list, and for each node, we check if it is already in the set. If it is, then it is the starting node of the cycle, and we return it. If not, we add it to the set and continue to the next node. If we reach the end of the list without finding a cycle, we return None.

Optimal Approach:

The optimal approach to find the starting node of the cycle is to use Floyd's cycle-finding algorithm, also known as the "tortoise and hare" algorithm. The algorithm consists of two pointers, slow and fast. The slow pointer moves one step at a time, while the fast pointer moves two steps at a time.

If there is no cycle in the linked list, the fast pointer will eventually reach the end of the list, and we can return None. If there is a cycle, the fast pointer will eventually catch up to the slow pointer, and they will meet at some point inside the cycle.

Once they meet, we reset the slow pointer to the head of the list and keep the fast pointer where it is. Now, both pointers move one step at a time until they meet again. The point where they meet will be the starting node of the cycle.

The reason why this works is that when the slow pointer enters the cycle, the fast pointer is already inside the cycle, ahead of the slow pointer. The fast pointer moves two steps at a time, so it will eventually catch up to the slow pointer.

Here's the Python code for the optimal approach:"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        slow = head
        fast = head

        # Step 1: Check if there is a cycle
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                break
        else:
            # No cycle, return None
            return None

        # Step 2: Find the starting node of the cycle
        slow = head
        while slow != fast:
            slow = slow.next
            fast = fast.next

        return slow


"""
This solution has a time complexity of O(n), where n is the number of nodes in the linked list. The space complexity is O(1) since we are using only a constant amount of extra space for the two pointers.
"""
