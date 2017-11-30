#  Given two binary strings, return their sum (also a binary string).

# For example,
# a = "11"
# b = "1"
# Return "100". 

class Solution:
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        al, bl = len(a), len(b)
        carry = 0
        res = ""
        for i in range(1, max(al, bl) + 1):
            x = int(a[-i]) if i <= al else 0
            y = int(b[-i]) if i <= bl else 0
            carry, tmp = divmod(x + y + carry, 2)
            res = str(tmp) + res
        if carry:
            res = str(carry) + res
        return res
            

# fastest
class Solution:
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        return bin(int(a, 2)+int(b, 2))[2:]
