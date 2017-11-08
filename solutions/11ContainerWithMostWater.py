# Given n non-negative integers a1, a2, ..., an, where each represents a point at coordinate (i, ai). n vertical lines are drawn such that the two endpoints of line i is at (i, ai) and (i, 0). Find two lines, which together with x-axis forms a container, such that the container contains the most water.

# Note: You may not slant the container and n is at least 2. 

class Solution:
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        left, right = 0, len(height) - 1
        maxValue = 0
        while left != right:
            if height[left] > height[right]:
                high = height[right]
                right -= 1
            else:
                high = height[left]
                left += 1
            currentValue = (right - left + 1) * high
            maxValue = maxValue if maxValue > currentValue else currentValue
        return maxValue
