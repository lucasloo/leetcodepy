

# Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

# (i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).

# You are given a target value to search. If found in the array return its index, otherwise return -1.

# You may assume no duplicate exists in the array.

# my solution, not very sure about the rotation part, requested result is just search around the list
class Solution:
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        # pivot = 0
        # for tmp in range(len(nums) - 1):
        #     if nums[tmp] > nums[tmp + 1]:
        #         pivot = tmp + 1
        # nums = nums[pivot:] + nums[0:pivot]
        for tmp in range(len(nums)):
            if nums[tmp] == target:
                return tmp
        return -1
