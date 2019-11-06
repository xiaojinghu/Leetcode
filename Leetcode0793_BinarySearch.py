class Solution(object):
    '''
    idea: To count how many 0s there are in x! is to count how many (2,5) pairs there are in x!'s factortial decomposition. Since 5 appears more rarely than 5, then actually it is to count how many 5s there are in x!'s factotial decomposition.
    Suppose x = 125, then we can find all multipliers of 5, which are 5,25,125, then we have 3 fives. If we devide them by five, we get 1,5,25, here we have 2 fives. Then we devide them by five, we get 1, and 5, so we have 1 five. In total we have 3+2+1 = 6 fives.
    If we denote the count of 5 for x as dp[x], then we have dp[1], dp[2], dp[3], dp[4] = 0,0,0,0
    dp[x] = x/5 + dp[x/5]
   '''
    def count(self, num, dp):
        # find the largest
        if num in dp:
            return dp[num]
        dp[num] = num/5 + self.count(num/5, dp)
        return dp[num]
    
    def preimageSizeFZF(self, K):
        """
        :type K: int
        :rtype: int
        """
        if K==0:
            return 5
        dp= {1:0, 2:0, 3:0, 4:0}
        left = K
        right = 5*(K+1)
        while(left+1<right):
            middle = (left+right)/2
            countOfFive = self.count(middle, dp)
            if countOfFive == K:
                # we know that dp[num] is a nondescending array and as long as some number p satisfies p/5 == num/5, then it shares the same K with num. We know that there must be 4 other p.
                return 5
            if countOfFive < K:
                left = middle
            else:
                right = middle
        if self.count(left, dp) == K or self.count(right, dp) == K:
            return 5
        return 0

            