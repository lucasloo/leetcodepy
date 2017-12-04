#  Follow up for "Remove Duplicates":
# What if duplicates are allowed at most twice?

# For example,
# Given sorted array nums = [1,1,1,2,2,3],

# Your function should return length = 5, with the first five elements of nums being 1, 1, 2, 2 and 3. It doesn't matter what you leave beyond the new length. 

class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        lastWord, twiceFlag, i = None, False, 0
        while i < len(nums):
            if lastWord != nums[i]:
                lastWord, twiceFlag = nums[i], False
                i += 1
            elif lastWord == nums[i]:
                if not twiceFlag:
                    twiceFlag = True
                    i += 1
                else:
                    nums.pop(i)
        return len(nums)


# concise and fastest

def removeDuplicates(self, nums):
    i = 0
    for n in nums:
        if i < 2 or n > nums[i-2]:
            nums[i] = n
            i += 1
    return i
