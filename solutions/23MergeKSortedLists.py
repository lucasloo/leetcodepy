# Merge k sorted linked lists and return it as one sorted list. Analyze and describe its complexity. 

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        storeDict = {}
        dummyNode = ListNode(None)
        currentNode = dummyNode
        for tmpNode in lists:
            self.putNodeInDict(storeDict, tmpNode)
        while len(storeDict) != 0:
            minVal = None
            for key in storeDict:
                if minVal == None or minVal > key:
                    minVal = key
            minNodeList = storeDict.pop(minVal)
            for minNode in minNodeList:
                currentNode.next = minNode
                currentNode = currentNode.next
                self.putNodeInDict(storeDict, minNode.next)
        return dummyNode.next
    
    def putNodeInDict(self, storeDict, tmpNode):
        if tmpNode:
            if tmpNode.val in storeDict:
                storeDict[tmpNode.val].append(tmpNode)
            else:
                storeDict[tmpNode.val] = [tmpNode]


# fastest solution and much more concise
class Solution:
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        arr = []
        new = ListNode(0)
        head = new
        for l in lists:
            while l:
                arr.append(l.val)
                l = l.next
    
        for val in sorted(arr):
            new.next = ListNode(val)
            new = new.next
            
        head = head.next
        return head
