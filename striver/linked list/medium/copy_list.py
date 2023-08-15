class Node:
    def __init__(self, x, next=None, random=None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        if not head:
            return None

        # Step 1: Duplicate each node and insert it right after the original node
        current = head
        while current:
            new_node = Node(current.val)
            new_node.next = current.next
            current.next = new_node
            current = new_node.next

        # Step 2: Set the random pointers of the new nodes
        current = head
        while current:
            if current.random:
                current.next.random = current.random.next
            current = current.next.next

        # Step 3: Extract the new linked list from the modified linked list
        new_head = head.next
        current = head
        while current:
            duplicate = current.next
            current.next = duplicate.next
            if duplicate.next:
                duplicate.next = duplicate.next.next
            current = current.next

        return new_head


"""
Explanation:
This code implements the deep copy of a linked list that contains random pointers. It follows the three-step approach mentioned earlier:

In Step 1, it creates deep nodes of all the original nodes and points them to the next of the corresponding original nodes.

In Step 2, it sets the random pointers of the deep nodes as per the  original list.

In Step 3, it separates the original linked list from the deep nodes list using three pointers (dummy, current, and deep_node). The dummy node is used to connect the deep nodes list, and the current pointer iterates through the original list to adjust the next pointers of the original nodes. The deep_node pointer helps in setting the next pointers of the deep nodes.

Finally, it returns the head of the deep copied linked list."""
