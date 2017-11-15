#  Given a linked list, swap every two adjacent nodes and return its head.

# For example,
# Given 1->2->3->4, you should return the list as 2->1->4->3.

# Your algorithm should use only constant space. You may not modify the values in the list, only nodes itself can be changed. 

class Solution:
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        dummyNode = ListNode(None)
        dummyNode.next = head
        currentNode = dummyNode
        while currentNode.next != None and currentNode.next.next != None:
            tmp = currentNode.next.next.next
            currentNode.next.next.next = currentNode.next
            currentNode.next = currentNode.next.next
            currentNode.next.next.next = tmp
            currentNode = currentNode.next.next
        return dummyNode.next
