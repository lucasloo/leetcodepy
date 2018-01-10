#Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

#(i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).

#Find the minimum element.

#You may assume no duplicate exists in the array.
class Solution:
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left, right = 0, len(nums) - 1
        while left < right:
            mid = (left + right) // 2
            if nums[mid] < nums[0]:
                right = mid
            else:
                left = mid + 1
        res = min(nums[0], nums[right])
        return res
    
