"""

Explanation:

To check if a linked list is a palindrome, we need to compare the values of nodes from the beginning and the end of the list. The basic approach to solve this problem is to reverse the second half of the linked list and then compare it with the first half.

Brute Force Approach:

Traverse the linked list and create an array to store the values of the nodes.
Check if the array is a palindrome (i.e., the values read the same from both ends of the array).
Optimal Approach:

To solve the problem in O(1) extra memory space, we can use the following steps:

Find the middle node of the linked list using the slow and fast pointer technique.
Reverse the second half of the linked list.
Compare the first half and the reversed second half of the linked list.
Let's implement the code for the optimal approach:"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def isPalindrome(self, head):
        # Helper function to reverse a linked list
        def reverse_linked_list(node):
            prev = None
            while node:
                next_node = node.next
                node.next = prev
                prev = node
                node = next_node
            return prev

        # Find the middle node of the linked list
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # Reverse the second half of the linked list
        second_half = reverse_linked_list(slow)

        # Compare the first half and the reversed second half
        while second_half:
            if head.val != second_half.val:
                return False
            head = head.next
            second_half = second_half.next

        return True


# Test cases
if __name__ == "__main__":
    # Test case 1
    head1 = ListNode(1)
    head1.next = ListNode(2)
    head1.next.next = ListNode(2)
    head1.next.next.next = ListNode(1)
    sol = Solution()
    print(sol.isPalindrome(head1))  # Output: True

    # Test case 2
    head2 = ListNode(1)
    head2.next = ListNode(2)
    sol = Solution()
    print(sol.isPalindrome(head2))  # Output: False


"""
The time complexity of this approach is O(n), where n is the number of nodes in the linked list. We traverse the linked list once to find the middle node and reverse the second half. The space complexity is O(1) since we only use a constant amount of extra memory for pointer manipulation."""
