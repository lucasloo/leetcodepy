#  Given an unsorted integer array, find the first missing positive integer.

# For example,
# Given [1,2,0] return 3,
# and [3,4,-1,1] return 2.

# Your algorithm should run in O(n) time and uses constant space. 


# sort it first, but violate the O(n) condition
class Solution:
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        mark = 0
        for i in range(len(nums)):
            if nums[i] > 0 and nums[i] <= mark + 1:
                mark = nums[i]
        return mark + 1

# fastest method, use the min and max to generate an order to scan through the set once, fit with O(n)
class Solution:
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 1
        only_positives = [i for i in nums if i >= 0]
        min_value = min(min(only_positives), 1) 
        max_value = max(only_positives)
        set_n = set(only_positives)
        for i in range(min_value, max_value):
            if i not in set_n:
                return i
        return max_value + 1 
