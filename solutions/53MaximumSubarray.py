#  Find the contiguous subarray within an array (containing at least one number) which has the largest sum.

# For example, given the array [-2,1,-3,4,-1,2,1,-5,4],
# the contiguous subarray [4,-1,2,1] has the largest sum = 6. 

class Solution:
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left = right = 0
        maxSum = nums[0]
        while right < len(nums):
            currentSum = nums[left] if left == right else currentSum + nums[right]
            maxSum = currentSum if currentSum > maxSum else maxSum
            if currentSum <= 0:
                left = right = right + 1
            else:
                right += 1
        return maxSum

# after reading the fastest solution, find out that left right record is not needed

class Solution:
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        runningSum=0
        maxSum=0
        for elt in nums:
            runningSum+=elt
            if runningSum>maxSum:
                maxSum=runningSum
            if runningSum<0:
                runningSum=0
        if maxSum==0 and runningSum==0:
            return max(nums)
        else:
            return maxSum
