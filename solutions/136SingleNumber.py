# Given an array of integers, every element appears twice except for one. Find that single one.

class Solution:
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        store = set()
        for i in nums:
            if i in store:
                store.remove(i)
            else:
                store.add(i)
        return store.pop()
class Solution:
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return_num = 0
        for element in nums:
            return_num ^= element
        return return_numclass Solution:
