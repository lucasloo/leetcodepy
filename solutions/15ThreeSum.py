# Given an array S of n integers, are there elements a, b, c in S such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.

# Note: The solution set must not contain duplicate triplets.

# For example, given array S = [-1, 0, 1, 2, -1, -4],

# A solution set is:
# [
#   [-1, 0, 1],
#   [-1, -1, 2]
# ]


class Solution:
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        resultList = []
        nums.sort()
        if len(nums) < 3:
            return resultList
        for i in range(len(nums) - 2):
            if i - 1 >= 0 and nums[i - 1] == nums[i]:
                continue
            if nums[i] > 0:
                return resultList
            low, high = i + 1, len(nums) - 1
            while low < high:
                s = nums[i] + nums[low] + nums[high]
                if s == 0:
                    resultList.append([nums[i], nums[low], nums[high]])
                    low += 1
                    high -= 1
                    while low < high and nums[low] == nums[low - 1]:
                        low += 1
                    while low < high and nums[high] == nums[high + 1]:
                        high -= 1
                elif s > 0:
                    high -= 1
                elif s < 0:
                    low += 1
        return resultList
