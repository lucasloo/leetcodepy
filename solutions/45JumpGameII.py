#  Given an array of non-negative integers, you are initially positioned at the first index of the array.

# Each element in the array represents your maximum jump length at that position.

# Your goal is to reach the last index in the minimum number of jumps.

# For example:
# Given array A = [2,3,1,1,4]

# The minimum number of jumps to reach the last index is 2. (Jump 1 step from index 0 to 1, then 3 steps to the last index.)

# Note:
# You can assume that you can always reach the last index.

class Solution:
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        visitedSet = {0}
        reachSet = {0}
        step = 0
        while len(reachSet) != 0 and len(nums) - 1 not in reachSet:
            tmpSet = reachSet.copy()
            reachSet.clear()
            step += 1
            for i in tmpSet:
                for k in range(1, nums[i] + 1):
                    if i + k < len(nums) and i + k not in visitedSet
                        reachSet.add(i + k)
                        visitedSet.add(i + k)
        return step
# Time limit (takes shit ton of Time) 
# my solution is stupid beacause the second for loop is unnecessary, the only thing need to do is to reach the farest point. Also, it is unnecessary to store all the nodes in the set, all I need is just a range, because range between start point and end point are all accessable

class Solution:
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        start = end = nextEnd = step = 0
        while end < len(nums) - 1:
            step += 1
            for i in range(start, end + 1):
                if i + nums[i] >= len(nums) - 1:
                    return step
                nextEnd = max(nextEnd, i + nums[i])
            start, end = end + 1, nextEnd
        return step
