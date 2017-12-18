# Given an array of integers, every element appears three times except for one, which appears exactly once. Find that single one.

class Solution:
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        a = set()
        b = set()
        for i in nums:
            if i in a:
                b.discard(i)
            else:
                a.add(i)
                b.add(i)
        return b.pop()



class Solution:
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return (int)((3*sum(set(nums)) - sum(nums)) / 2)
