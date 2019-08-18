class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        # No priority
        # the calculation can be done sequencially
        stack = []
        i = 0
        while(i<len(s)):
            if s[i].isdigit():
                # we get the complete number and push it into the stack
                num = ""
                while(i<len(s) and s[i].isdigit()):
                    num += s[i]
                    i += 1
                stack.append(int(num))
                continue
            if s[i] == '(':
                # we push it into the stack and continue
                stack.append(s[i])
                i += 1
                continue
            if s[i] == '+':
                stack.append(s[i])
                i += 1
                continue
            if s[i] == '-':
                # we push it into the stack and continue
                stack.append(s[i])
                i += 1
                continue
            if s[i] == ')':
                # we pop from the stack till we meet '('
                Sum = 0
                while(stack[-1]!='('):
                    num = stack.pop()
                    if stack[-1] == '+':
                        stack.pop()
                        Sum += num
                    if stack[-1] == '-':
                        stack.pop()
                        Sum -= num
                    if stack[-1] == '(':
                        stack.pop()
                        Sum += num
                        break
                stack.append(Sum)
                i += 1
                continue
            # empty spaces
            i += 1
            continue
        print stack
        Sum = 0  
        sign = 1
        for i in range(len(stack)):
            if stack[i] == '+':
                sign = 1
                i += 1
                continue
            if stack[i] == '-':
                sign = -1
                i += 1
                continue
            Sum += stack[i]*sign
            i += 1
        return Sum