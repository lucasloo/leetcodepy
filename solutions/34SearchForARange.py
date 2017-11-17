# Given an array of integers sorted in ascending order, find the starting and ending position of a given target value.

# Your algorithm's runtime complexity must be in the order of O(log n).

# If the target is not found in the array, return [-1, -1].

# For example,
# Given [5, 7, 7, 8, 8, 10] and target value 8,
# return [3, 4]. 

class Solution:
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        head, tail = 0, len(nums) - 1
        middle = (tail + head) // 2
        while head < tail:
            if nums[middle] == target:
                break
            elif nums[middle] > target:
                tail = middle - 1
            else:
                head = middle + 1
            middle = (tail + head) // 2
        if len(nums) <= 0 or nums[middle] != target:
            return [-1, -1]
        left = right = middle
        while left - 1 >= 0 and nums[left - 1] == nums[middle]:
            left -= 1
        while right + 1 < len(nums) and nums[right + 1] == nums[middle]:
            right += 1
        return [left, right]


# recommend solution
class Solution:
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        lo = bisect.bisect_left(nums, target)
        return [lo, bisect.bisect(nums, target)-1] if target in nums[lo:lo+1] else [-1, -1]
