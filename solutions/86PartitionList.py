# Given a linked list and a value x, partition it such that all nodes less than x come before nodes greater than or equal to x.

# You should preserve the original relative order of the nodes in each of the two partitions.

# For example,
# Given 1->4->3->2->5->2 and x = 3,
# return 1->2->2->4->3->5. 

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        l, r = ListNode(None), ListNode(None)
        lc, rc, c = l, r, head
        while c != None:
            if c.val < x:
                lc.next = c
                lc = lc.next
            else:
                rc.next = c
                rc = rc.next
            c = c.next
        lc.next = r.next
        rc.next = None
        return l.next
            
        
