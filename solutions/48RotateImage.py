# You are given an n x n 2D matrix representing an image.

# Rotate the image by 90 degrees (clockwise).

# Note:
# You have to rotate the image in-place, which means you have to modify the input 2D matrix directly. DO NOT allocate another 2D matrix and do the rotation.

# Example 1:

# Given input matrix = 
# [
#   [1,2,3],
#   [4,5,6],
#   [7,8,9]
# ],

# rotate the input matrix in-place such that it becomes:
# [
#   [7,4,1],
#   [8,5,2],
#   [9,6,3]
# ]

# Example 2:

# Given input matrix =
# [
#   [ 5, 1, 9,11],
#   [ 2, 4, 8,10],
#   [13, 3, 6, 7],
#   [15,14,12,16]
# ], 

# rotate the input matrix in-place such that it becomes:
# [
#   [15,13, 2, 5],
#   [14, 3, 4, 1],
#   [12, 6, 8, 9],
#   [16, 7,10,11]
# ]
class Solution:
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        def rotateLayer(matrix, n):
            if n >= len(matrix) - n - 1:
                return
            for i in range(n, len(matrix) - 1 - n):
                x, y = i, n
                tmp = matrix[y][x]
                for _ in range(4):
                    tmp1 = matrix[x][len(matrix) - 1 - y]
                    matrix[x][len(matrix) - 1 - y] = tmp
                    tmp = tmp1
                    y, x = x, len(matrix) - 1 - y
            rotateLayer(matrix, n + 1)
        rotateLayer(matrix, 0)
