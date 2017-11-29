# Given a list, rotate the list to the right by k places, where k is non-negative.

# Example:

# Given 1->2->3->4->5->NULL and k = 2,

# return 4->5->1->2->3->NULL.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        current = head
        storeList = []
        while current != None:
            storeList.append(current)
            current = current.next
        if len(storeList) <= 1:
            return head
        k = k % len(storeList)
        if k == 0:
            return head
        res = storeList[-k]
        storeList[-k - 1].next = None
        storeList[-1].next = head
        return res
