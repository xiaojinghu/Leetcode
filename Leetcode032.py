class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s)<=1:
            return 0
        
        maxLen = 0
        
        #from left to right
        left = 0
        right = 0
        for i in range(len(s)):
            if s[i] == '(':
                left += 1
            else:
                right += 1
            if left<right:
                left = 0
                right = 0
                continue
            if left == right:
                maxLen = max(maxLen, 2*right)
                
        # from right to left
        left = 0
        right = 0
        for i in range(len(s)-1, -1, -1):
            if s[i] == ')':
                left += 1
            else:
                right += 1
            if left<right:
                left = 0
                right = 0
                continue
            if left == right:
                maxLen = max(maxLen, 2*right)
                
        return maxLen