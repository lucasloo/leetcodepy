# Given a singly linked list L: L0→L1→…→Ln-1→Ln,
# reorder it to: L0→Ln→L1→Ln-1→L2→Ln-2→…

# You must do this in-place without altering the nodes' values.

# For example,
# Given {1,2,3,4}, reorder it to {1,4,2,3}. 
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: void Do not return anything, modify head in-place instead.
        """
        if not head or not head.next or not head.next.next:
            return
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        slow.next, head2 = None, slow.next
        dummy = ListNode(None)
        while head2:
            tmp, head2 = head2, head2.next
            tmp.next = dummy.next
            dummy.next = tmp
        head2 = dummy.next
        current = head
        while current:
            if head2:
                tmp = current.next
                current.next = head2
                head2 = head2.next
                current.next.next = tmp
                current = current.next.next
            else:
                break

