#  Given an array of non-negative integers, you are initially positioned at the first index of the array.

# Each element in the array represents your maximum jump length at that position.

# Determine if you are able to reach the last index.

# For example:
# A = [2,3,1,1,4], return true.

# A = [3,2,1,0,4], return false. 

class Solution:
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        point = right = 0
        if right == len(nums) - 1:
            return True
        while not(point == right and nums[point] == 0):
            right = max(right, nums[point] + point)
            point += 1
            if right >= len(nums) - 1:
                return True
        return False

# reverse
class Solution:
    def canJump(self, nums):
        last_index = len(nums) - 1
        for i in reversed(range(last_index)):
            if i + nums[i] >= last_index:
                last_index = i
        return last_index == 0
