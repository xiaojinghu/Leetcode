class Solution(object):
    def backtrack(self, s, path, res):
        if len(path) == 4 and not s:
            res.append('.'.join(path))
        if not s:
            return
        minDigit = min(3, len(s))
        for i in range(minDigit):
            if i == 0:
                self.backtrack(s[1:], path+[str(s[i])], res)
                continue
            if s[0] == '0':
                break
            if 0<int(s[:i+1])<=255:
                self.backtrack(s[i+1:], path+[str(s[:i+1])], res)
                
                    
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        if len(s)>12:
            return []
        res = []
        self.backtrack(s, [],res)
        return res
        