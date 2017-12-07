#  A message containing letters from A-Z is being encoded to numbers using the following mapping:

# 'A' -> 1
# 'B' -> 2
# ...
# 'Z' -> 26

# Given an encoded message containing digits, determine the total number of ways to decode it.

# For example,
# Given encoded message "12", it could be decoded as "AB" (1 2) or "L" (12).

# The number of ways decoding "12" is 2. 

class Solution:
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        def dfs(s):
            if len(s) == 0:
                return 1
            if len(s) == 1:
                return 1 if s[-1] != "0" else 0
            if s[0] == "0":
                return 0
            elif int(s[0:2]) > 0 and int(s[0:2]) <= 26:
                n = dfs(s[1:]) + dfs(s[2:])
                return n
            elif int(s[0:2]) > 26:
                return dfs(s[1:])
        if len(s) == 0:
            return 0
        return dfs(s)
# using dfs exceeded time limit

class Solution(object):
    def numDecodings(self, s):
        if not len(s) or s[0] == '0':
            return 0
        total = 1
        pre = 1
        for i in range(1, len(s)):
            if s[i] == '0':
                if not s[i-1] in '12':
                    return 0
                total = pre
                continue
            elif int(s[i-1:i+1]) < 27 and s[i-1] != '0':
                pre, total = total, total+pre
            else:
                pre = total
        return total
