# Given an integer n, generate a square matrix filled with elements from 1 to n2 in spiral order.

# For example,
# Given n = 3,
# You should return the following matrix:

# [
#  [ 1, 2, 3 ],
#  [ 8, 9, 4 ],
#  [ 7, 6, 5 ]
# ]
class Solution:
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        def generateLayer(matrix, nums, i):
            if len(nums) == 0:
                return
            x = y = i
            if len(nums) == 1:
                matrix[x][y] = nums[0]
                return
            while y < len(matrix) and matrix[x][y] == 0:
                matrix[x][y] = nums.pop()
                y += 1
            y -= 1
            x += 1
            while x < len(matrix) and matrix[x][y] == 0:
                matrix[x][y] = nums.pop()
                x += 1
            x -= 1
            y -= 1
            while y >= 0 and matrix[x][y] == 0:
                matrix[x][y] = nums.pop()
                y -= 1
            y += 1
            x -= 1
            while x >= 0 and matrix[x][y] == 0:
                matrix[x][y] = nums.pop()
                x -= 1
            generateLayer(matrix, nums, i + 1)
        nums = [i for i in reversed(range(1, n ** 2 + 1))]
        matrix = [[0 for _ in range(n)] for _ in range(n)]
        generateLayer(matrix, nums, 0)
        return matrix

# inside-out rotate
def generateMatrix(self, n):
    A, lo = [], n*n+1
    while lo > 1:
        lo, hi = lo - len(A), lo
        A = [range(lo, hi)] + zip(*A[::-1])
    return A
