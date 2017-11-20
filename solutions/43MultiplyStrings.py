# Given two non-negative integers num1 and num2 represented as strings, return the product of num1 and num2.

# Note:

#     The length of both num1 and num2 is < 110.
#     Both num1 and num2 contains only digits 0-9.
#     Both num1 and num2 does not contain any leading zero.
#     You must not use any built-in BigInteger library or convert the inputs to integer directly.


class Solution:
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        res = 0
        for x in range(len(num1)):
            tmpRes = 0
            for y in range(len(num2)):
                tmpRes = tmpRes * 10 + int(num1[x]) * int(num2[y])
            res = res * 10 + tmpRes
        return str(res)


