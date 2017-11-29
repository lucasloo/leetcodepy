# Given a non-negative integer represented as a non-empty array of digits, plus one to the integer.

# You may assume the integer do not contain any leading zero, except the number 0 itself.

# The digits are stored such that the most significant digit is at the head of the list.

class Solution:
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        carry = 1
        for i in range(1, len(digits) + 1):
            tmp = digits[-i] + carry
            carry = tmp // 10
            digits[-i] = tmp % 10
            if carry == 0:
                break
        if carry:
            return [1] + digits
        else:
            return digits
            

# concise
class Solution:
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        sumDigits = int("".join(str(num) for num in digits)) + 1
        return [int(num) for num in str(sumDigits)]
        
