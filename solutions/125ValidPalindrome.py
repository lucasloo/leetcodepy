#  Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

# For example,
# "A man, a plan, a canal: Panama" is a palindrome.
# "race a car" is not a palindrome.

# Note:
# Have you consider that the string might be empty? This is a good question to ask during an interview.

# For the purpose of this problem, we define empty string as valid palindrome. 

class Solution:
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        l, r = 0, len(s) - 1
        s = s.lower()
        def isAlphanumeric(c):
            return True if "a" <= c <= "z" or "0" <= c <= "9" else False
        while l < r:
            if not isAlphanumeric(s[l]):
                l += 1
                continue
            if not isAlphanumeric(s[r]):
                r -= 1
                continue
            if s[l] != s[r]:
                return False
            l += 1
            r -= 1
        return True
            
                
class Solution:
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        import re
        s = re.sub(r'[^A-Za-z0-9]', '', s).lower()
        return s == s[::-1]
