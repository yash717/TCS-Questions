"""
Question Explanation:

You are given two sorted linked lists, list1 and list2. Your task is to merge these two lists into a single sorted list. The merged list should contain all the nodes from both list1 and list2, while maintaining the sorted order. You need to return the head of the merged linked list.

Brute Force Approach:

The brute force approach involves creating a new linked list and iteratively comparing the nodes from both list1 and list2. We will keep adding the smaller node to the new merged list and move the respective pointer in that list to the next node. Once one of the lists is completely merged, we will add the remaining nodes from the other list, if any.

Optimal Approach:

The optimal approach takes advantage of the fact that both list1 and list2 are already sorted. We can merge them in a way that we compare the nodes only when needed, and we do not need to create a new merged list explicitly. Instead, we can modify the pointers of the original nodes to create the merged list.

Code Implementation (Brute Force Approach):"""

# Definition for singly-linked list.


class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def mergeTwoLists(self, list1, list2):
        # Initialize the dummy node for the merged list
        dummy = ListNode(-1)
        current = dummy

        # Loop until both lists are not empty
        while list1 and list2:
            # Compare the values of the current nodes from both lists
            if list1.val <= list2.val:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next

            # Move the current pointer in the merged list to the next node
            current = current.next

        # Add any remaining nodes from list1 or list2, if any
        if list1:
            current.next = list1
        else:
            current.next = list2

        # Return the head of the merged list (skip the dummy node)
        return dummy.next


"""
Explanation of the Brute Force Code:

The code defines the ListNode class, representing a node in the singly linked list. Each node has a val attribute and a next pointer pointing to the next node in the list.

The Solution class contains the method mergeTwoLists to merge the two sorted linked lists.

The function takes list1 and list2 as input, which are the heads of the sorted linked lists, and returns the head of the merged list.

We create a dummy node with value -1 as the starting point for the merged list. We will keep modifying the next pointers to construct the merged list.

We use the current pointer to keep track of the last node in the merged list, starting from the dummy node.

We use a while loop to merge the two lists. The loop continues as long as both list1 and list2 are not empty.

Inside the loop, we compare the values of the current nodes from both lists. If the value of list1 is less than or equal to the value of list2, we add the node from list1 to the merged list. Otherwise, we add the node from list2.

We then move the respective pointer in the original list (either list1 or list2) to the next node, and we move the current pointer in the merged list to the next node as well.

The loop continues, and we keep adding nodes from the lists until one of the lists becomes empty.

After the loop, we add any remaining nodes from list1 or list2, if any, to the merged list.

Finally, we return the head of the merged list, which is the next node after the dummy node."""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        # when list1 is empty then
        # our output will be same as list2
        if l1 == None:
            return l2

        # when list2 is empty then our output
        # will be same as list1
        if l2 == None:
            return l1

        # pointing l1 and l2 to smallest and greatest one
        if l1.val > l2.val:
            l1, l2 = l2, l1

        # act as head of resultant merged list
        res = l1

        while l1 != None and l2 != None:
            temp = None
            while l1 != None and l1.val <= l2.val:
                temp = l1  # storing last sorted node
                l1 = l1.next
            # link previous sorted node with
            # next larger node in list2
            temp.next = l2
            l1, l2 = l2, l1
        return res


"""
Yes, the provided code is another approach to merge two sorted linked lists and it's a valid solution. It follows an iterative approach with three pointers: l1, l2, and temp. The code effectively rearranges the pointers to merge the two lists in a sorted manner.

Explanation of the Code:

The code defines the Solution class, which contains the method mergeTwoLists. The method takes two input parameters, l1 and l2, which are the heads of the two sorted linked lists to be merged.

The function starts with two base cases to handle the scenarios where one of the input lists is empty. If l1 is empty, it directly returns l2. If l2 is empty, it directly returns l1.

The code then checks which list's head node has the smaller value, and it assigns l1 and l2 accordingly to ensure l1 always points to the list with the smaller first element.

The variable res is used to store the head of the merged list, which initially points to the head of the smaller list (l1).

The code enters a while loop that continues until either l1 or l2 becomes None.

Within the loop, there is another nested while loop that iterates through l1 until it finds a node whose value is greater than the first node of l2. This temp variable points to the last sorted node in l1.

After finding the appropriate position, the code links the temp.next (the last sorted node in l1) to l2. This effectively merges the current segment of l1 with l2.

The l1 and l2 pointers are then swapped, allowing the loop to continue the merging process.

The process continues until either l1 or l2 becomes None.

Finally, the function returns the head of the merged list (res), which contains the merged nodes in sorted order.

Is This the Better Approach?

The provided code follows an iterative approach to merge two sorted linked lists, and it is a valid and efficient approach. The time complexity of this approach is O(m + n), where m and n are the lengths of l1 and l2, respectively, because each node is visited once. The space complexity is O(1) since the merging is done in-place without using any additional data structures.

Overall, the code is a good solution to the problem and offers an efficient way to merge two sorted linked lists without using extra space."""
