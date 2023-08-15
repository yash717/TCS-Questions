# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def mergeTwoLists(self, first, second):
        if first == None:
            return second
        if second == None:
            return first

        if first.val > second.val:
            first, second = second, first

        res = first

        while first != None and second != None:
            temp = None
            while first != None and first.val <= second.val:
                temp = first
                first = first.next
            temp.next = second
            first, second = second, first
        return res
