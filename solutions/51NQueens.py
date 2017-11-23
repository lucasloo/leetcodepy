# The n-queens puzzle is the problem of placing n queens on an n×n chessboard such that no two queens attack each other.

# Given an integer n, return all distinct solutions to the n-queens puzzle.

# Each solution contains a distinct board configuration of the n-queens' placement, where 'Q' and '.' both indicate a queen and an empty space respectively.

# For example,
# There exist two distinct solutions to the 4-queens puzzle:

# [
#  [".Q..",  // Solution 1
#   "...Q",
#   "Q...",
#   "..Q."],

#  ["..Q.",  // Solution 2
#   "Q...",
#   "...Q",
#   ".Q.."]
# ]

class Solution:
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        def placeQueen(currentQueensList, currentBoardList, x, resList):
            if x == len(currentBoardList):
                resList.append(currentQueensList)
                return
            for y in range(len(currentBoardList[x])):
                if currentBoardList[x][y] != 0:
                    continue
                else:
                    newQueensList = currentQueensList.copy()
                    newQueensList.append(y)
                    newBoardList = [tmp.copy() for tmp in currentBoardList]
                    alterBoard(newBoardList, x, y)
                    placeQueen(newQueensList, newBoardList, x + 1, resList)
        def convertResList(n, resList):
            res = []
            for tmpList in resList:
                subRes = []
                for i in tmpList:
                    s = ""
                    for _ in range(i):
                        s += "."
                    s += "Q"
                    for _ in range(n - i - 1):
                        s += "."
                    subRes.append(s)
                res.append(subRes)
            return res
        def alterBoard(currentBoardList, x, y):
            for i in range(len(currentBoardList)):
                currentBoardList[x][i] = 1
                currentBoardList[i][y] = 1
            n = 1
            length = len(currentBoardList)
            while x + n < length and y + n < length:
                currentBoardList[x + n][y + n] = 1
                n += 1
            n = 1
            while x + n < length and y - n >= 0:
                currentBoardList[x + n][y - n] = 1
                n += 1
            n = 1
            while x - n >= 0 and y + n < length:
                currentBoardList[x - n][y + n] = 1
                n += 1
            n = 1
            while x - n >= 0 and y - n >= 0:
                currentBoardList[x - n][y - n] = 1
                n += 1
        currentBoardList = [[0 for _ in range(n)] for _ in range(n)]
        currentQueensList = []
        resList = []
        placeQueen(currentQueensList, currentBoardList, 0, resList)
        return convertResList(n, resList)
        

# fast and consice
class Solution:
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        def DFS(queens, xy_dif, xy_sum):
            p = len(queens)
            if p==n:
                result.append(queens)
                return None
            for q in range(n):
                if q not in queens and p-q not in xy_dif and p+q not in xy_sum: 
                    DFS(queens+[q], xy_dif+[p-q], xy_sum+[p+q])  
        result = []
        DFS([],[],[])
        return [ ["."*i + "Q" + "."*(n-i-1) for i in sol] for sol in result]
