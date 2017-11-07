#Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.

#Example:

#Input: "babad"

#Output: "bab"

#Note: "aba" is also a valid answer.

#Example:

#Input: "cbbd"

#Output: "bb"


class Solution:
    
    _low = 0
    
    _high = 0
    
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        for i in range(len(s)):
            self.extendPalindrome(s, i, i)
            self.extendPalindrome(s, i, i + 1)
        return s[self._low : self._high + 1]
        
        
    def extendPalindrome(self, s, head, tail):
        while head >= 0 and tail < len(s) and s[head] == s[tail]:
            tail += 1
            head -= 1
        tail -= 1
        head += 1
        if tail - head > self._high - self._low:
            self._high, self._low = tail, head

class RecommendSolution:
    # @return a string
    def longestPalindrome(self, s):
        if len(s)==0:
        	return 0
        maxLen=1
        start=0
        for i in range(len(s)):
        	if i-maxLen >=1 and s[i-maxLen-1:i+1]==s[i-maxLen-1:i+1][::-1]:
        		start=i-maxLen-1
        		maxLen+=2
        		continue

        	if i-maxLen >=0 and s[i-maxLen:i+1]==s[i-maxLen:i+1][::-1]:
        		start=i-maxLen
        		maxLen+=1
        return s[start:start+maxLen]
