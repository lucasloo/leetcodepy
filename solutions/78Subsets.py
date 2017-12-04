#  Given a set of distinct integers, nums, return all possible subsets (the power set).

# Note: The solution set must not contain duplicate subsets.

# For example,
# If nums = [1,2,3], a solution is:

# [
#   [3],
#   [1],
#   [2],
#   [1,2,3],
#   [1,3],
#   [2,3],
#   [1,2],
#   []
# ]
class Solution:
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        def DFS(nums, current):
            res.append(current)
            if len(nums) == 0:
                return
            for i in range(len(nums)):
                DFS(nums[i + 1:], current + [nums[i]])
        res = []
        DFS(nums, [])
        return res

# concise
class Solution:
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = [[]]
        for num in nums:
            res += [i + [num] for i in res]
        return res
