class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        if not s:
            return True
        for char in s:
            if not stack:
                stack.append(char)
                continue
            if char in '([{':
                stack.append(char)
                continue
            if char == '}':
                if stack[-1]!='{':
                    return False
                stack.pop()
                continue
            if char == ']':
                if stack[-1]!='[':
                    return False
                stack.pop()
                continue
            if char == ')':
                if stack[-1]!='(':
                    return False
                stack.pop()
                continue
        return not stack
