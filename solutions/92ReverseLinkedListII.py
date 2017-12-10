# Reverse a linked list from position m to n. Do it in-place and in one-pass.
#
# For example:
# Given 1->2->3->4->5->NULL, m = 2 and n = 4,
#
# return 1->4->3->2->5->NULL.
#
# Note:
# Given m, n satisfy the following condition:
# 1 ≤ m ≤ n ≤ length of list.


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        dummy = ListNode(None)
        dummy.next, current, reverseL = head, dummy, None
        for _ in range(1, m):
            current = current.next
        tail = current.next
        for _ in range(m, n):
            tmp = current.next
            current.next = current.next.next
            tmp.next = reverseL
            reverseL = tmp
            tail.next = current.next.next
        if m < n:
            current.next.next = reverseL
        return dummy.next

