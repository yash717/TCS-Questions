"""
Problem Explanation:

Given a singly-linked list head and a node node that needs to be deleted, we are not given access to the first node of the linked list. The task is to delete the given node while ensuring that the linked list maintains its integrity. By deleting the node, we mean that the value of the given node should not exist in the linked list, and the number of nodes in the linked list should decrease by one. Additionally, all the values before node should be in the same order, and all the values after node should be in the same order.

Brute Force Approach:

A brute-force approach to delete a node without access to the head of the linked list would be to traverse the entire list starting from the head until we find the previous node of the given node. Once we find the previous node, we can change its next pointer to skip the node and point directly to the node after node. This way, we effectively remove the given node from the linked list.

Optimal Approach:

Since we do not have access to the head of the linked list, we cannot traverse the list in a conventional way to find the previous node of the given node. However, we can achieve the desired deletion by copying the data from the next node of the node into the node, effectively overwriting the value of the node. After that, we can skip the next node, achieving the same effect as removing the node.

Optimal Solution:"""


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def deleteNode(self, node):
        # Copy the data from the next node into the current node
        node.val = node.next.val
        # Skip the next node by updating the next pointer of the current node
        node.next = node.next.next


"""
The above deleteNode function takes a node that needs to be deleted and modifies it in-place to remove it from the linked list. It follows the optimal approach by copying the data from the next node into the current node and then skipping the next node by updating the next pointer of the current node.

This solution guarantees a time complexity of O(1) since we only perform constant-time operations to delete the node, and a space complexity of O(1) since we are not using any additional data structures."""
