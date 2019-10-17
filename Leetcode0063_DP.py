class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        dp = [[0]*len(obstacleGrid[0]) for i in range(len(obstacleGrid))]
        # initialize the DP
        if obstacleGrid[len(obstacleGrid)-1][len(obstacleGrid[0])-1] == 0:
            dp[len(obstacleGrid)-1][len(obstacleGrid[0])-1] = 1  
        else:
            dp[len(obstacleGrid)-1][len(obstacleGrid[0])-1] = 0
        
        for i in range(len(obstacleGrid)-1, -1, -1):
            for j in range(len(obstacleGrid[0])-1, -1, -1):
                if obstacleGrid[i][j] == 1:
                    dp[i][j] = 0
                    continue
                #move right or down
                if i+1<len(obstacleGrid):
                    if obstacleGrid[i+1][j] == 0:
                        dp[i][j] += dp[i+1][j]
                if j+1<len(obstacleGrid[0]):
                    if obstacleGrid[i][j+1] == 0:
                        dp[i][j] += dp[i][j+1]
                # print dp
        # print dp
        return dp[0][0]
