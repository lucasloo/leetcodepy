# Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:

#     Integers in each row are sorted from left to right.
#     The first integer of each row is greater than the last integer of the previous row.

# For example,

# Consider the following matrix:

# [
#   [1,   3,  5,  7],
#   [10, 11, 16, 20],
#   [23, 30, 34, 50]
# ]

# Given target = 3, return true.

# my solution is to treat the 2D matrix as a list
class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not (matrix and matrix[0]):
            return False
        l = len(matrix) * len(matrix[0])
        left, right = 0, l - 1
        while left <= right:
            mid = (left + right) // 2
            value = matrix[mid // len(matrix[0])][mid % len(matrix[0])]
            if value == target:
                return True
            elif value > target:
                right = mid - 1
            else:
                left = mid + 1
        return False
        
