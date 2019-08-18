class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        # No priority
        # the calculation can be done sequencially
        # res is used to store the current calculation result
        res = 0
        # num is the number we are operating on
        num = 0
        # sign is the sign of the current operator
        sign = 1
        #put things between '()' into the stack'
        stack = []
        for c in s:
            print stack
            if c.isdigit():
                num = 10*num+int(c)
                continue
            if c == '+' or c == '-':
                res += sign*num
                num = 0
                sign = 1 if c=='+' else -1
                continue
            if c == '(':
                # push the former result into the stack
                stack.append(res)
                # push the sign into the stack
                stack.append(sign)
                res = 0
                num = 0
                sign = 1
                continue
            if c == ')':
                res += sign*num
                num = 0
                res *= stack.pop()
                res += stack.pop()
                continue
        res += num*sign
        return res