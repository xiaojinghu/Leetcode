class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        # DP solution
        # Suppose dp[i][j] is the answer of the sub-problem of i+1, j+1. Then we have the following trasfer function:
        # dp[i][j] += dp[i][j-1]+dp[i-1][j]
        # Initialization
        dp = []
        for i in range(m):
            dp.append([0]*n)
        for j in range(n):
            dp[0][j] = 1
        for i in range(m):
            dp[i][0] = 1
        # print dp
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] += dp[i][j-1]+dp[i-1][j]
        return dp[m-1][n-1]
                    