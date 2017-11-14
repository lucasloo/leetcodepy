# Given an array S of n integers, are there elements a, b, c, and d in S such that a + b + c + d = target? Find all unique quadruplets in the array which gives the sum of target.

# Note: The solution set must not contain duplicate quadruplets.

# For example, given array S = [1, 0, -1, 0, -2, 2], and target = 0.

# A solution set is:
# [
#   [-1,  0, 0, 1],
#   [-2, -1, 1, 2],
#   [-2,  0, 0, 2]
# ]


# My solution; correct answer but exceed time limit
class Solution:
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        nums.sort()
        left, right = 0, len(nums) - 1
        result = []
        while left < len(nums) - 3:
            right = len(nums) - 1
            while right >= left + 3:
                left1, right1 = left + 1, right - 1
                while left1 < right1:
                    fourSum = nums[left] + nums[right] + nums[left1] + nums[right1]
                    if fourSum <= target:
                        if fourSum == target:
                            result.append([nums[left],nums[right], nums[left1], nums[right1]])
                        left1 += 1
                        while left1 < right1 and nums[left1] == nums[left1 - 1]:
                            left1 += 1
                    else:
                        right1 -= 1
                        while left1 < right1 and nums[right1] == nums[right1 + 1]:
                            right1 -= 1
                right -= 1
                while left < right and nums[right] == nums[right + 1]:
                    right -= 1
            left += 1
            while left < len(nums) - 3 and nums[left] == nums[left - 1]:
                left += 1
        return result
        
