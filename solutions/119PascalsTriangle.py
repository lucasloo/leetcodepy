# Given an index k, return the kth row of the Pascal's triangle.

# For example, given k = 3,
# Return [1,3,3,1].

# Note:
# Could you optimize your algorithm to use only O(k) extra space? 

class Solution:
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        res = [1]
        for _ in range(rowIndex):
            last = 0
            for i in range(len(res)):
                tmp = res[i]
                res[i] += last
                last = tmp
            res.append(1)
        return res
