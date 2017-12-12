# Given numRows, generate the first numRows of Pascal's triangle.

# For example, given numRows = 5,
# Return

# [
#      [1],
#     [1,1],
#    [1,2,1],
#   [1,3,3,1],
#  [1,4,6,4,1]
# ]


class Solution:
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        res = []
        for i in range(1, numRows + 1):
            tmp = []
            for n in range(i):
                if n == 0 or n == i - 1:
                    tmp.append(1)
                else:
                    tmp.append(res[-1][n - 1] + res[-1][n])
            res.append(tmp)
        return res
        
