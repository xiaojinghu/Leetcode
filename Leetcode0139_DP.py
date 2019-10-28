class Solution(object):     
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        # THIS IS A DP SOLUTION
        wordDict = set(wordDict)
        # dp[i] records whether s[:i] is breakable
        dp = [False]*(len(s)+1)
        dp [0] = True
        for i in range(1, len(s)+1):
            for j in range(0,i):
                # here we split s[:i] into two parts
                # s[:j] and s[j:i]
                if dp[j] and (s[j:i] in wordDict):
                    dp[i] = True
                    break
        return dp[len(s)]