# Follow up for N-Queens problem.

# Now, instead outputting board configurations, return the total number of distinct solutions.


class Solution:
    def __init__(self):
        self.res = 0
    
    def totalNQueens(self, n):
        """
        :type n: int
        :rtype: int
        """       
        self.DFS(n, [], [], [])
        return self.res
    
    def DFS(self, n, xySum, xyDif, queenPosList):
            if n == len(queenPosList):
                self.res += 1
                return
            for i in range(n):
                if i not in queenPosList and i + len(queenPosList) not in xySum and i - len(queenPosList) not in xyDif:
                    self.DFS(n, xySum + [i + len(queenPosList)], xyDif + [i - len(queenPosList)], queenPosList + [i])  


