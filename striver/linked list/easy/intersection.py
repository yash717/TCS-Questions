"""
To find the intersection point of two linked lists, we can use the following approach:

Brute Force Approach:

Traverse through one linked list (headA) and store the references of all nodes in a set.
Traverse through the second linked list (headB) and for each node, check if it already exists in the set. If it does, that's the intersection point, so return the node.
If we reach the end of both linked lists without finding an intersection, return None.
Here's the brute force implementation:"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def getIntersectionNode(self, headA, headB):
        # Step 1: Traverse through one linked list (headA) and store nodes in a set
        node_set = set()
        while headA:
            node_set.add(headA)
            headA = headA.next

        # Step 2: Traverse through the second linked list (headB) and check if nodes exist in the set
        while headB:
            if headB in node_set:
                return headB
            headB = headB.next

        # Step 3: If no intersection found, return None
        return None


"""
Time complexity: O(m + n), where m and n are the lengths of the two linked lists. This is because we need to traverse both lists once to create the set and then to find the intersection.

Space complexity: O(m), where m is the length of the first linked list. This is because we need to store all nodes of the first linked list in the set."""


class Solution:
    def getIntersectionNode(self, headA, headB):
        # Take two dummy nodes for each list and point them to the heads
        dummyA, dummyB = ListNode(), ListNode()
        dummyA.next, dummyB.next = headA, headB

        # Iterate over the lists until they collide or both reach the end (become None)
        while headA != headB:
            # Move headA to the head of headB after reaching the end of headA
            headA = headA.next if headA else dummyB.next
            # Move headB to the head of headA after reaching the end of headB
            headB = headB.next if headB else dummyA.next

        return headA


""""
Explanation:

We define the Solution class with the method getIntersectionNode, which takes headA and headB as inputs and returns the intersection node if it exists.

We create two dummy nodes dummyA and dummyB, both pointing to None.

We set the next attribute of dummyA to headA, and the next attribute of dummyB to headB. This makes dummyA and dummyB act as "pointers" to the heads of headA and headB, respectively.

We start a loop that continues until headA and headB become the same (collide) or both reach the end of their respective lists (become None).

Inside the loop, we update headA and headB as follows:

If headA is not None, move headA to its next node; otherwise, move it to the head of headB.
If headB is not None, move headB to its next node; otherwise, move it to the head of headA.
The loop continues until headA and headB point to the same node (intersection point) or both become None.

After the loop, we return the intersection node (headA). If the lists have no intersection, headA will be None, and we will return None as required. Otherwise, we return the node at which the two lists intersect."""
