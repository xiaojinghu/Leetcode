class Solution(object):
    def backtrack(self, left, right, n, path, res):
        # termination condition
        if right>left or left>n or right>n:
            return 
        if left == n and right == n:
            res.append(path)
            return 
        # we must make sure that left>=right
        self.backtrack(left+1,right,n, path+'(',res)
        self.backtrack(left, right+1, n, path+')', res)       
        
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        res = []
        self.backtrack(0,0,n,"",res)
        return res
