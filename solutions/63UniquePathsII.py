# Follow up for "Unique Paths":

# Now consider if some obstacles are added to the grids. How many unique paths would there be?

# An obstacle and empty space is marked as 1 and 0 respectively in the grid.

# For example,

# There is one obstacle in the middle of a 3x3 grid as illustrated below.

# [
#   [0,0,0],
#   [0,1,0],
#   [0,0,0]
# ]

# The total number of unique paths is 2.

# Note: m and n will be at most 100.

class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        dp = [[1 for _ in range(len(obstacleGrid[0]))] for _ in range(len(obstacleGrid))]
        dp[0][0] = 1 - obstacleGrid[0][0]
        for x in range(1, len(obstacleGrid)):
            dp[x][0] = 1 if obstacleGrid[x][0] == 0 and dp[x - 1][0] else 0
        for y in range(1, len(obstacleGrid[0])):
            dp[0][y] = 1 if obstacleGrid[0][y] == 0 and dp[0][y - 1] else 0
        for x in range(1, len(obstacleGrid)):
            for y in range(1, len(obstacleGrid[0])):
                dp[x][y] = 0 if obstacleGrid[x][y] else dp[x - 1][y] + dp[x][y - 1]
        return dp[-1][-1]
