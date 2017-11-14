# Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

# The brackets must close in the correct order, "()" and "()[]{}" are all valid but "(]" and "([)]" are not.

class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        tmpPool = []
        parenthesesMap = {"{": "}", "[":"]", "(":")"}
        for tmpChar in s:
            if tmpChar in parenthesesMap:
                tmpPool.append(tmpChar)
            else:
                if len(tmpPool) == 0:
                    return False
                tmp = tmpPool.pop()
                if tmpChar != parenthesesMap[tmp]:
                    return False
        return False if len(tmpPool) else True
