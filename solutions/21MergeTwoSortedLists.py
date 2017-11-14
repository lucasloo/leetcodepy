# Merge two sorted linked lists and return it as a new list. The new list should be made by splicing together the nodes of the first two lists.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        dummyNode = ListNode(0)
        currentNode = dummyNode
        while l1 != None or l2 != None:
            if l1 == None:
                currentNode.next = l2
                break
            elif l2 == None:
                currentNode.next = l1
                break
            if l1.val >= l2.val:
                currentNode.next = l2
                currentNode = currentNode.next
                l2 = l2.next
            else:
                currentNode.next = l1
                currentNode = currentNode.next
                l1 = l1.next
        return dummyNode.next
        
