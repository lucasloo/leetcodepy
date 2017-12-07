#  Given a collection of integers that might contain duplicates, nums, return all possible subsets (the power set).

# Note: The solution set must not contain duplicate subsets.

# For example,
# If nums = [1,2,2], a solution is:

# [
#   [2],
#   [1],
#   [1,2,2],
#   [2,2],
#   [1,2],
#   []
# ]
class Solution:
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        numsMap = {}
        for i in nums:
            if i in numsMap:
                numsMap[i] += 1
            else:
                numsMap[i] = 1
        res = [[]]
        for i in numsMap:
            tmpRes = res.copy()
            for tmp in res:
                tmpCopy = tmp.copy()
                for k in range(numsMap[i]):
                    tmpCopy.append(i)
                    tmpRes.append(tmpCopy.copy())
            res = tmpRes
        return res
                    
