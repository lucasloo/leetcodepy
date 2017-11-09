#Write a function to find the longest common prefix string amongst an array of strings. 

class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        result, index = "", 0
        if len(strs) == 0:
            return result
        while True:
            tmpChar = ""
            for tmpStr in strs:
                if len(tmpStr) <= index:
                    return result 
                if tmpChar != "" and tmpChar != tmpStr[index]:
                    return result
                else: 
                    tmpChar = tmpStr[index]
            result += tmpChar
            index += 1
