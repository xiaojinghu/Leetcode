class Solution(object):
    def isValid(self, s):
        left = 0
        right = 0
        for char in s:
            if char == "(":
                left += 1
            if char == ")":
                right += 1
            if left<right:
                return False
        return left == right
    
    def helper(self, s, start, extraLeft, extraRight, res):
        # s is valid only if there is no extra left and no extra right
        if extraLeft == 0 and extraRight == 0:
            if self.isValid(s):
                res.append(s)
            return
        for i in range(start, len(s)):
            # we need to delete one letter from s and check if it is valid
            # to avoid repeated answor, for consecuitive '('s and ')'s, we need only delete the first one.
            if i!=start and s[i]==s[i-1]:
                continue
            if extraLeft>0 and s[i] == '(':
                self.helper(s[:i]+s[i+1:], i, extraLeft-1, extraRight, res)
            if extraRight>0 and s[i]==')':
                self.helper(s[:i]+s[i+1:], i, extraLeft, extraRight-1, res)
                
                
                
    def removeInvalidParentheses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        extraLeft = 0
        extraRight = 0
        for char in s:
            if char == '(':
                extraLeft += 1
            if char == ')':
                # extraRight appears only when extraLeft==0, otherwise they will match the extra left '('s
                if extraLeft == 0:
                    extraRight += 1
                else:
                    # we match the extra left with the current ')'
                    extraLeft -= 1
        res = []
        self.helper(s, 0, extraLeft, extraRight, res)
        return res
                    