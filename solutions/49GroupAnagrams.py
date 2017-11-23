# Given an array of strings, group anagrams together.

# For example, given: ["eat", "tea", "tan", "ate", "nat", "bat"],
# Return:

# [
#   ["ate", "eat","tea"],
#   ["nat","tan"],
#   ["bat"]
# ]

# Note: All inputs will be in lower-case.

class Solution:
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        matchMap = {}
        for i in strs:
            sortStr = "".join(sorted(i))
            if sortStr in matchMap:
                matchMap[sortStr].append(i)
            else:
                matchMap[sortStr] = [i]
        return list(matchMap.values())
                
