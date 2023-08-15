"""

Explanation:

The task is to add two numbers represented as linked lists and return the sum as a new linked list. The numbers are given in reverse order, meaning the least significant digit is at the head of each linked list.

To add the numbers, we can simulate the process of addition, starting from the least significant digit (head) of each linked list and moving towards the most significant digit (tail). As we traverse the linked lists, we add the corresponding digits along with any carry from the previous addition.

Brute Force Approach:

The brute force approach involves simulating the process of addition, digit by digit, while keeping track of the carry. We create a new linked list to store the sum and return it as the result.

Optimal Approach:

The optimal approach also simulates the process of addition, but instead of creating a new linked list, we modify one of the input linked lists to store the result. This reduces the need for creating extra nodes and improves space efficiency.

Brute Force Code:"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1, l2):
        # Initialize a dummy node as the starting node of the result linked list
        dummy = ListNode(0)
        # Initialize pointers to traverse l1, l2, and the result linked list
        curr = dummy
        p1, p2 = l1, l2
        # Initialize a carry variable to keep track of the carry during addition
        carry = 0

        # Traverse both linked lists
        while p1 or p2:
            # Get the values of the current nodes, or 0 if the nodes are None
            x = p1.val if p1 else 0
            y = p2.val if p2 else 0
            # Calculate the sum of current digits and the carry from the previous addition
            total = x + y + carry
            # Calculate the new carry for the next addition
            carry = total // 10
            # Create a new node with the sum of current digits and add it to the result linked list
            curr.next = ListNode(total % 10)
            # Move the pointers to the next nodes
            if p1:
                p1 = p1.next
            if p2:
                p2 = p2.next
            curr = curr.next

        # If there is still a carry after traversing both linked lists, add it as a new node
        if carry:
            curr.next = ListNode(carry)

        # Return the next node after the dummy node, which is the head of the result linked list
        return dummy.next


"""
Explanation of Optimal Solution:

The optimal solution modifies the input linked list l1 to store the sum. It traverses both l1 and l2 simultaneously, adding the corresponding digits and keeping track of the carry. The result is stored in l1 itself.

We use two pointers, p1 and p2, to traverse l1 and l2, respectively, and a variable carry to keep track of the carry during addition.

The loop continues until both p1 and p2 reach the end of their respective linked lists.

In each iteration, we calculate the sum of the current digits along with the carry from the previous addition. We update the value of the current node in l1 with the sum, and if l1 has no more nodes, we append the remaining nodes from l2 to l1.

We also store the previous node in prev to handle the case where l1 has fewer nodes than l2.

Finally, if there is still a carry after traversing both linked lists, we add it as a new node to the end of l1.

The solution guarantees a time complexity of O(max(m, n)) and a space complexity of O(1), where m and n are the lengths of l1 and l2, respectively. This is because we are modifying l1 in place and not using any additional data structures except for a few variables."""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1, l2):
        # Initialize pointers to traverse l1, l2, and the result linked list
        p1, p2, carry = l1, l2, 0

        # Traverse both linked lists
        while p1 or p2:
            # Get the values of the current nodes, or 0 if the nodes are None
            x = p1.val if p1 else 0
            y = p2.val if p2 else 0
            # Calculate the sum of current digits and the carry from the previous addition
            total = x + y + carry
            # Calculate the new carry for the next addition
            carry = total // 10
            # Update the value of the current node in l1 to store the result
            if p1:
                p1.val = total % 10
            else:
                # If l1 has no more nodes, append the remaining nodes from l2 to l1
                p1 = ListNode(total % 10)
                prev.next = p1
            # Store the previous node in l1 to handle the case where l1 has fewer nodes than l2
            prev = p1
            # Move the pointers to the next nodes
            p1 = p1.next if p1 else None
            p2 = p2.next if p2 else None

        # If there is still a carry after traversing both linked lists, add it as a new node
        if carry:
            prev.next = ListNode(carry)

        # Return the head of the modified l1, which contains the sum as a linked list
        return l1


# CODING NINJA SOLUTTION

class Node:
    def __init__(self, data=0, next=None):
        self.data = data
        self.next = next


def addTwoNumbers(head1: Node, head2: Node) -> Node:
    dummy = Node()  # Initialize a dummy node to handle the result linked list
    temp = dummy  # Initialize a pointer to traverse the result linked list
    carry = 0  # Initialize a carry variable to keep track of the carry during addition

    # Traverse both linked lists until both reach the end and the carry is 0
    while head1 or head2 or carry:
        # Calculate the sum of the current digits and the carry from the previous addition
        total = (head1.data if head1 else 0) + \
            (head2.data if head2 else 0) + carry
        # Calculate the new carry for the next addition
        carry = total // 10
        # Create a new node with the sum of current digits and add it to the result linked list
        temp.next = Node(total % 10)
        # Move the pointers to the next nodes
        temp = temp.next
        if head1:
            head1 = head1.next
        if head2:
            head2 = head2.next

    # Return the head of the result linked list, which is the next node after the dummy node
    return dummy.next
