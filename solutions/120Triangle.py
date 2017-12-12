# Given a triangle, find the minimum path sum from top to bottom. Each step you may move to adjacent numbers on the row below.

# For example, given the following triangle

# [
#      [2],
#     [3,4],
#    [6,5,7],
#   [4,1,8,3]
# ]

# The minimum path sum from top to bottom is 11 (i.e., 2 + 3 + 5 + 1 = 11).

# Note:
# Bonus point if you are able to do this using only O(n) extra space, where n is the total number of rows in the triangle. 

class Solution:
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        for i in range(len(triangle) - 1):
            for k in range(len(triangle[i])):
                if k == 0:
                    triangle[i + 1][k] += triangle[i][k]
                    triangle[i + 1][k + 1] += triangle[i][k] if k + 1 >= len(triangle[i]) else min(triangle[i][k], triangle[i][k + 1])
                elif k == len(triangle[i]) - 1:
                    triangle[i + 1][k + 1] += triangle[i][k]
                else:
                    triangle[i + 1][k + 1] += min(triangle[i][k], triangle[i][k + 1])
        return min(triangle[-1])


# buttom up

class Solution:
    def minimumTotal(self, triangle):
        result = [0 for i in range(0, len(triangle) + 1)]
        for row in triangle[::-1]:
            for i in range(0, len(row)):
                result[i] = row[i] + min(result[i], result[i + 1])
        return result[0]
