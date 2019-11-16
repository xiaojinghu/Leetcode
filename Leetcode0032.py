class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        #idea: traverse both from left and  right to find the longest valid parenthethese length
        if not s:
            return 0
        left1, right1, left2, right2, maxLen = 0,0,0,0,0
        for i in range(len(s)):
            currCharLeft = s[i]
            currCharRight = s[len(s)-1-i]
            # check the maximum left length
            # print i, left1, right1, left2, right2
            if currCharLeft == '(':
                # we can always add it
                left1 += 1
            else:
                right1 += 1
                #check if we can update the maxLen
                if left1 == right1:
                    maxLen = max(maxLen, 2*left1)
                # check if we need to reset left and right
                if right1>left1:
                    left1 = 0
                    right1 = 0
            # check thge maximum right length
            if currCharRight == ')':
                # we can always add it
                right2 += 1
            else:
                left2 += 1
                #check if we can update the maxLen
                if right2 == left2:
                    maxLen = max(maxLen, 2*right2)
                # check if we need to reset left and right
                if left2>right2:
                    right2 = 0
                    left2 = 0
        return maxLen