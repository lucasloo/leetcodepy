#  A self-dividing number is a number that is divisible by every digit it contains.

# For example, 128 is a self-dividing number because 128 % 1 == 0, 128 % 2 == 0, and 128 % 8 == 0.

# Also, a self-dividing number is not allowed to contain the digit zero.

# Given a lower and upper number bound, output a list of every possible self dividing number, including the bounds if possible.

# Example 1:

# Input: 
# left = 1, right = 22
# Output: [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 15, 22]

# Note:
# The boundaries of each input argument are 1 <= left <= right <= 10000.

class Solution:
    def selfDividingNumbers(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: List[int]
        """
        def checkSelfDividingNumbers(num):
            tmp, dividend = num, 0
            while tmp != 0:
                diviend = tmp % 10
                tmp = tmp // 10
                if diviend == 0 or i % diviend != 0:
                    return False
            return True
        
        res = []
        for i in range(left, right + 1):
            if checkSelfDividingNumbers(i):
                res.append(i)
        return res

# Although mine is faster， but the lambda aproach below is so elegent
class Solution(object):
    def selfDividingNumbers(self, left, right):
        is_self_dividing = lambda num: '0' not in str(num) and all(num % int(digit) == 0 for digit in str(num))
        return list(filter(is_self_dividing, range(left, right + 1)))
