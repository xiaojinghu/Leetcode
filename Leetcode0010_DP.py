class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        dp = []
        # dp[i][j] denotes whether s[:i] matches p[:j]
        for i in range(len(s)+1):
            dp.append([False]*(len(p)+1))
        dp[0][0] = True
        
        # we know that for any i>0, dp[i][0] = False, so we can start j from 1.
        for i in range(len(s)+1):
            for j in range(1, len(p)+1):
                # here we need to calculate dp[i][j] which is to check whether s[:i] matches p[:j]. 
                # Case1: p[j-1] is a letter or '.'
                if p[j-1]!='*':
                    # the case of i==0 is ommited because the default value of dp[i][j] is false.
                    if i>0 and p[j-1] in [s[i-1], '.'] and dp[i-1][j-1]:
                        dp[i][j] = True
                    continue
                # Case2: p[j-1] is '*'
                if p[j-1] == '*':
                    # p[j-2] must exists and  is a '.' or a letter
                    # if we match 0 p[j-2]
                    if dp[i][j-2]:
                        dp[i][j] = True
                        continue
                    # if we match 1 p[j-2]
                    if dp[i][j-1]:
                        dp[i][j] = True
                        continue
                    # if we match multiple p[j-2]
                    if i>0 and p[j-2] in [s[i-1], '.'] and dp[i-1][j]:
                        dp[i][j] = True
        # print dp                   
        return dp[len(s)][len(p)]