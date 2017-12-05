#  Given a sorted linked list, delete all nodes that have duplicate numbers, leaving only distinct numbers from the original list.

# For example,
# Given 1->2->3->3->4->4->5, return 1->2->5.
# Given 1->1->1->2->3, return 2->3. 

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        dummy = ListNode(None)
        dummy.next = head
        if not head:
            return head
        last, current, nextNode = dummy, head, head.next
        while nextNode != None:
            if nextNode.val == current.val:
                while nextNode != None and nextNode.val == current.val:
                    nextNode = nextNode.next
                last.next = nextNode
                current = nextNode
                nextNode = current.next if current else None
            else:
                last = current
                current = nextNode
                nextNode = current.next
        return dummy.next
