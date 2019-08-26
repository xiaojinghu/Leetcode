class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if not grid:
            return 0
        
        dp = [[0]*len(grid[0]) for i in range(len(grid))]
        dp[0][0] = grid[0][0]
        
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                # print dp
                if i == 0 and j == 0:
                    continue
                if i == 0:
                    dp[i][j] = dp[i][j-1]+grid[i][j]
                    continue
                if j == 0:
                    dp[i][j] = dp[i-1][j]+grid[i][j]
                    continue
                dp[i][j] = min(dp[i-1][j], dp[i][j-1])+grid[i][j]
        
        return dp[-1][-1]