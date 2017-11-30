# Given a m x n matrix, if an element is 0, set its entire row and column to 0. Do it in place. 

class Solution:
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        xl, yl = set(), set()
        for x in range(len(matrix)):
            for y in range(len(matrix[0])):
                if matrix[x][y] == 0:
                    xl.add(x)
                    yl.add(y)
        for x in xl:
            for i in range(len(matrix[0])):
                matrix[x][i] = 0
        for y in yl:
            for i in range(len(matrix)):
                matrix[i][y] = 0
