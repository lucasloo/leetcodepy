#  Given two integers n and k, return all possible combinations of k numbers out of 1 ... n.

# For example,
# If n = 4 and k = 2, a solution is:

# [
#   [2,4],
#   [3,4],
#   [2,3],
#   [1,2],
#   [1,3],
#   [1,4],
# ]
class Solution:
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        def DFS(nums, i, current):
            if i == 0:
                res.append(current)
                return
            if i > len(nums):
                return
            for index in range(len(nums)):
                DFS(nums[index + 1:], i - 1, current + [nums[index]])
        res = []
        DFS([i for i in range(1, n + 1)], k, [])
        return res

# import itertools
from itertools import combinations

class Solution:
    def combine(self, n, k):
        return list(combinations(range(1, n+1), k))
