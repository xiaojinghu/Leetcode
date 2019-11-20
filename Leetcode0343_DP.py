class Solution(object):
    def integerBreak(self, n):
        """
        :type n: int
        :rtype: int
        """
        # DP
        # 1. Base cases:
        #    2 = 1+1
        #    3 = 1+2
        #    4 = 2+2
        # 2. general cases: n>=5
        #    when n>=5, we con split t into 
        #    (1, n-1)
        #    (2, n-2)
        #    (3, n-1)
        #    ...
        # suppose dp[i] means the maximum product we can get from i, then
        # dp[i] = max([dp[i-j]*dp[j-1], dp[i],j*(i+1-j), j*dp[i-j], dp[j-1]*(i+1-j)])
        
        # initialize the dp. dp[0] means currently the sum is 1, ..., dp[i] means currently the sum is i+1.
        # and since we can always split i+1 into 1 and i when n>=2, dp[i] always has a minimim value of i
        dp = range(n)
        dp[0] = 1
        # for simplicity, we set dp[0] as 1
        for i in range(1, n):
            for j in range(1, (i+1)/2+1):
                dp[i] = max([dp[i-j]*dp[j-1], dp[i],j*(i+1-j), j*dp[i-j], dp[j-1]*(i+1-j)])
        # print dp
        return dp[n-1]