#  Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it is able to trap after raining.

# For example,
# Given [0,1,0,2,1,0,1,3,2,1,2,1], return 6. 

class Solution:
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        maxLeft = maxRight = res = 0
        left, right = 0, len(height) - 1
        while left <= right:
            if maxRight >= maxLeft:
                if height[left] >= maxLeft:
                    maxLeft = height[left]
                else:
                    res += maxLeft - height[left]
                left += 1
            else:
                if height[right] >= maxRight:
                    maxRight = height[right]
                else:
                    res += maxRight - height[right]
                right -= 1
        return res
