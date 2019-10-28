class Solution(object):
    def dfs(self, s, wordDict, memo):
        # Termination condition
        if s in memo:
            return memo[s]
        if not s or s in wordDict:
            memo[s] = True
            return True
        if len(s) == 1 and s not in wordDict:
            memo[s] = False
            return False
        for i in range(1, len(s)):
            if s[:i] in wordDict and self.dfs(s[i:], wordDict, memo):
                memo[s] = True
                return True
        memo[s] = False
        return False
      
        
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        wordDict = set(wordDict)
        memo = {}
        return self.dfs(s, wordDict, memo)
        