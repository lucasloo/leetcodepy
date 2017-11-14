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
       
# devide the problem into finding 2 sums
class Solution:
    def fourSum(self, nums, target):
        def findNsum(nums, target, N, result, results):
            if len(nums) < N or N < 2 or target < nums[0]*N or target > nums[-1]*N:
                return
            if N == 2:
                l,r = 0,len(nums)-1
                while l < r:
                    s = nums[l] + nums[r]
                    if s == target:
                        results.append(result + [nums[l], nums[r]])
                        l += 1
                        while l < r and nums[l] == nums[l-1]:
                            l += 1
                    elif s < target:
                        l += 1
                    else:
                        r -= 1
            else:
                for i in range(len(nums)-N+1):
                    if i == 0 or (i > 0 and nums[i-1] != nums[i]):
                        findNsum(nums[i+1:], target-nums[i], N-1, result+[nums[i]], results)
        results = []
        findNsum(sorted(nums), target, 4, [], results)
        return results
         
