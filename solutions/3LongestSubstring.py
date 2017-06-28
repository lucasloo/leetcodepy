# Given a string, find the length of the longest substring without repeating characters.

# Examples:

# Given "abcabcbb", the answer is "abc", which the length is 3.

# Given "bbbbb", the answer is "b", with the length of 1.

# Given "pwwkew", the answer is "wke", with the length of 3. Note that the answer must be a substring, "pwke" is a subsequence and not a substring.

# My solution (sliding window)
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        head, tail, maxLen = 0, 0, 0
        content = {}
        while head < len(s):
            if s[head] in content:
                tail = tail if content[s[head]] + 1 < tail else content[s[head]] + 1
            content[s[head]] = head
            maxLen = maxLen if maxLen > head - tail + 1 else head - tail + 1
            head += 1
        return maxLen