# Implement int sqrt(int x).

# Compute and return the square root of x.

# x is guaranteed to be a non-negative integer.

class Solution:
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        r = x
        while r*r > x:
            r = (r + x/r) // 2
        return int(r)
