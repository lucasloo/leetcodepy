#  Given a collection of distinct numbers, return all possible permutations.

# For example,
# [1,2,3] have the following permutations:

# [
#   [1,2,3],
#   [1,3,2],
#   [2,1,3],
#   [2,3,1],
#   [3,1,2],
#   [3,2,1]
# ]


class Solution:
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        def permuteCursive(nums, current, res):
            if len(nums) == 0:
                res.append(current)
                return
            for i in range(len(nums)):
                leftNums = nums.copy()
                tmp = leftNums.pop(i)
                currentCopy = current.copy()
                currentCopy.append(tmp)
                permuteCursive(leftNums, currentCopy, res)
        res = []
        current = []
        permuteCursive(nums, current, res)
        return res
