# Given a roman numeral, convert it to an integer.

# Input is guaranteed to be within the range from 1 to 3999.

class Solution:
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        romanMap = {'M': 1000,'D': 500 ,'C': 100,'L': 50,'X': 10,'V': 5,'I': 1}
        result = 0
        for index in range(len(s) - 1):
            if romanMap[s[index]] < romanMap[s[index + 1]]:
                result -= romanMap[s[index]]
            else:
                result += romanMap[s[index]]
        return result + romanMap[s[-1]]
