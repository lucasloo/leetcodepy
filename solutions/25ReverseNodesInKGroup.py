#  Given a linked list, reverse the nodes of a linked list k at a time and return its modified list.

# k is a positive integer and is less than or equal to the length of the linked list. If the number of nodes is not a multiple of k then left-out nodes in the end should remain as it is.

# You may not alter the values in the nodes, only nodes itself may be changed.

# Only constant memory is allowed.

# For example,
# Given this linked list: 1->2->3->4->5

# For k = 2, you should return: 2->1->4->3->5

# For k = 3, you should return: 3->2->1->4->5 

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        def checkLen(head, k):
            """
            :type head: ListNode
            :type k: int
            :rtype: Bool
            """
            n = 0
            while head != None:
                head = head.next
                n += 1
                if n >= k:
                    break
            return True if n >= k else False
        
        def reverse(head, k):
            """
            :type head: ListNode
            :type k: int
            :rtype: (newHeadNode, tailNode)
            """
            dummyNode = ListNode(None)
            dummyNode.next = head
            nextNode = head.next
            for _ in range(k - 1):
                head.next = nextNode.next
                nextNode.next = dummyNode.next
                dummyNode.next = nextNode
                nextNode = head.next
            return (dummyNode.next, head)
        
        dummyNode = ListNode(None)
        lastTailNode = dummyNode
        currentNode = head
        if not checkLen(currentNode, k):
            return head
        while checkLen(currentNode, k):
            currentNode, tail = reverse(currentNode, k)
            lastTailNode.next = currentNode
            lastTailNode = tail
            currentNode = tail.next
        return dummyNode.next


# using recursive

class Solution:
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if not head :
            return head
        count = 1
        curr = head
        
        while curr and count<k :
            curr = curr.next
            count += 1
    
        if not curr :
            return head
        
        nxt = curr.next
        curr.next = None
        curr = head
        prev = None
        while curr :
            temp = curr.next
            curr.next = prev
            prev =  curr
            curr = temp
            
        head.next = self.reverseKGroup(nxt,k)
        return prev
