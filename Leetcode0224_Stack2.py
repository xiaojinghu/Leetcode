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
            if c.isdigit():
                num = 10*num+int(c)
                continue
            if c == '+':
                res += sign*num
                sign = 1
                num = 0
                continue
            if c=='-':
                res += num*sign
                sign = -1
                num = 0
                continue
            if c == '(':
                # we push the current result into the stack
                stack.append(res)
                # we push the current sign into the stack
                stack.append(sign)
                # reinitialize res, num and sign
                # to calcalculate the result in '()'
                res = 0
                num = 0
                sign = 1
                continue
            if c == ')':
                res  += num *sign
                # now we finished calculating things in the "()", we need to add it with the previous result
                sign = stack.pop()
                res = sign * res + stack.pop()
                # now we need initialize num 
                num = 0
                continue
        # note we have not finished calculating because the last number hasn't been added
        res += num*sign
        return res
