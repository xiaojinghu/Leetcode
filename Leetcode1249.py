class Solution(object):
    def minRemoveToMakeValid(self, s):
        """
        :type s: str
        :rtype: str
        """
        # FORWARD
        left = 0
        right = 0
        rmRight = set() 
        for i in range(len(s)):
            char = s[i]
            if char.isalpha():
                continue
            if char == '(':
                left += 1
                continue
            if char == ')':
                if right==left:
                    rmRight.add(i)
                    continue
                else:
                    right += 1
        # BACKWARD
        left = 0
        right = 0
        res = ""
        for i in range(len(s)-1, -1, -1):
            char = s[i]
            if i in rmRight:
                continue
            if char.isalpha():
                res = char+res
            if char == ')':
                right += 1
                res = ')'+res
                continue
            if char == '(':
                if left==right:
                    continue
                else:
                    left += 1
                    res = '(' + res
        return res
        