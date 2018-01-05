# Given an input string, reverse the string word by word.
# 
# For example,
# Given s = "the sky is blue",
# return "blue is sky the". 

import re
class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        res = re.split(r'\s+', s)
        res = res[::-1]
        return ' '.join([i for i in res if i != ""])
