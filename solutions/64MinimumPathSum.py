# Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right which minimizes the sum of all numbers along its path.

# Note: You can only move either down or right at any point in time.

# Example 1:

# [[1,3,1],
#  [1,5,1],
#  [4,2,1]]

# Given the above grid map, return 7. Because the path 1→3→1→1→1 minimizes the sum. 

class Solution:
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        for x in range(1, len(grid)):
            grid[x][0] += grid[x - 1][0]
        for y in range(1, len(grid[0])):
            grid[0][y] += grid[0][y - 1]
        for x in range(1, len(grid)):
            for y in range(1, len(grid[0])):
                grid[x][y] += min(grid[x - 1][y], grid[x][y -1])
        return grid[-1][-1]
    
