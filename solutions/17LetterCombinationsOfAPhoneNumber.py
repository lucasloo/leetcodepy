# Given a digit string, return all possible letter combinations that the number could represent.

# A mapping of digit to letters (just like on the telephone buttons) is given below.

# Input:Digit string "23"
# Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].

class Solution:
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        digitsMap = {"0":"0", "1":"1", "2":"abc", "3":"def", "4":"ghi", "5":"jkl", "6":"mno", "7":"pqrs", "8":"tuv", "9":"wxyz"}
        result = []
        tmpList = [""]
        for tmpChar in digits:
            result.clear()
            chars = digitsMap[tmpChar]
            for c in chars:
                for originStr in tmpList:
                    result.append(originStr + c)
            tmpList = result.copy()
        return result
