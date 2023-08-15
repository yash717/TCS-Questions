"""

Explanation:

This problem is about detecting cycles in a linked list. A cycle is a situation where a node in the linked list points to a previous node, creating a loop. We need to determine if such a cycle exists in the given linked list.

Brute Force Approach:

A brute force approach would involve using a set or a hashmap to keep track of visited nodes. We can traverse the linked list, and at each node, check if the node is already present in the set. If it is, then there is a cycle in the linked list, and we return True. If we reach the end of the linked list without finding any cycle, we return False.

The time complexity of this approach is O(n), where n is the number of nodes in the linked list. The space complexity is also O(n) since we need to store all visited nodes in the set.

Optimal Approach:

To solve this problem with O(1) space complexity, we can use Floyd's Cycle Detection Algorithm (also known as the "tortoise and hare" algorithm). This algorithm uses two pointers, one moving at a slower pace (tortoise) and the other at a faster pace (hare).

We start both pointers at the head of the linked list.
The tortoise moves one step at a time, and the hare moves two steps at a time.
If there is a cycle in the linked list, the hare will eventually catch up to the tortoise, and they will meet at some point.
If there is no cycle, the hare will reach the end of the linked list, and we can return False.
Let's implement the optimal approach using the tortoise and hare pointers:"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        # Initialize the tortoise and hare pointers
        tortoise = head
        hare = head

        # Traverse the linked list using the tortoise and hare pointers
        while hare and hare.next:
            tortoise = tortoise.next
            hare = hare.next.next

            # If the hare catches up to the tortoise, there is a cycle
            if tortoise == hare:
                return True

        # If the hare reaches the end, there is no cycle
        return False
