#  Given a collection of numbers that might contain duplicates, return all possible unique permutations.

# For example,
# [1,1,2] have the following unique permutations:

# [
#   [1,1,2],
#   [1,2,1],
#   [2,1,1]
# ]
class Solution:
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        def permuteCursive(numsMap, currentList, res):
            if len(numsMap) == 0:
                res.append(currentList)
            for i in numsMap:
                numsMapCopy = numsMap.copy()
                currentListCopy = currentList.copy()
                if numsMapCopy[i] == 1:
                    del numsMapCopy[i]
                else:
                    numsMapCopy[i] -= 1
                currentListCopy.append(i)
                permuteCursive(numsMapCopy, currentListCopy, res)
        numsMap = {}
        res = []
        for i in nums:
            numsMap[i] = numsMap[i] + 1 if i in numsMap else 1
        permuteCursive(numsMap, [], res)
        return res
