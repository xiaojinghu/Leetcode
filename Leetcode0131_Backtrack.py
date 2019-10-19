class Solution(object):
    def isPalindrome(self,s):
        i = 0
        j = len(s)-1
        while(i<j):
            if s[i] != s[j]:
                return False
            i += 1
            j -= 1
        return True
    
    
    def dfs(self, s, path, res):
        # termination condition
        if not s:
            res.append(path)
            return
        # we need to discompose s
        for i in range(1, len(s)+1):
            # pruning
            if self.isPalindrome(s[:i]):
                self.dfs(s[i:], path+[s[:i]], res)
        return
        
            
        
       
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        res = []
        self.dfs(s, [], res)
        return res
        