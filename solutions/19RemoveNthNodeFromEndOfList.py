# Given a linked list, remove the nth node from the end of list and return its head.

# For example,

#    Given linked list: 1->2->3->4->5, and n = 2.

#    After removing the second node from the end, the linked list becomes 1->2->3->5.

# Note:
# Given n will always be valid.
# Try to do this in one pass. 


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        storeList = []
        currentNode = head
        while currentNode != None:
            storeList.append(currentNode)
            currentNode = currentNode.next
        if len(storeList) == n:
            return storeList[0].next
        storeList[-n - 1].next = storeList[-n].next
        return head

# Another aproach using fast pointer and slow pointer

class Solution:
    def removeNthFromEnd(self, head, n):
        fast = slow = head
        for _ in range(n):
            fast = fast.next
        if not fast:
            return head.next
        while fast.next:
            fast = fast.next
            slow = slow.next
        slow.next = slow.next.next
        return head
