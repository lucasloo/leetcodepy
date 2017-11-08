# Given an integer, convert it to a roman numeral.

# Input is guaranteed to be within the range from 1 to 3999.

class Solution:
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        romanList = [""]*4
        romanList[0] = ["","I","II","III","IV","V","VI","VII","VIII","IX"]
        romanList[1] = ["","X","XX","XXX","XL","L","LX","LXX","LXXX","XC"]
        romanList[2] = ["","C","CC","CCC","CD","D","DC","DCC","DCCC","CM"]
        romanList[3] = ["","M","MM","MMM"]
        result = ""
        result += romanList[3][num // 1000]
        num = num % 1000
        result += romanList[2][num // 100]
        num = num % 100
        result += romanList[1][num // 10]
        num = num % 10
        result += romanList[0][num]
        return result
