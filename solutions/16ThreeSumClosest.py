# Given an array S of n integers, find three integers in S such that the sum is closest to a given number, target. Return the sum of the three integers. You may assume that each input would have exactly one solution.

#     For example, given array S = {-1 2 1 -4}, and target = 1.

#     The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).

class Solution:
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        minRange, result = abs(nums[0] + nums[1] + nums[-1] - target), nums[0] + nums[1] + nums[-1]
        for i in range(len(nums) - 2):
            left, right = i + 1, len(nums) - 1
            while left < right:
                tmpSum = nums[i] + nums[left] + nums[right]
                tmpRange = abs(tmpSum - target)
                if tmpRange == 0:
                    return target
                elif tmpSum > target:
                    right -= 1
                    while right >= 0 and nums[right] == nums[right + 1]:
                        right -= 1
                else:
                    left += 1
                    while left < len(nums) and nums[left] == nums[left - 1]:
                        left += 1
                if tmpRange < minRange:
                    minRange, result = tmpRange, tmpSum
        return result
