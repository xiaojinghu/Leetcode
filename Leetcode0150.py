class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        if not tokens:
            return None
        
        
        stack = []
        
        n = len(tokens)
        i = 0
        while(i<n):
            token = tokens[i]
            if token == "+":
                num1 = stack.pop()
                num2 = stack.pop()
                stack.append(num1+num2)
                i += 1
                continue
            if token == "-":
                num1 = stack.pop()
                num2 = stack.pop()
                stack.append(num2-num1)
                i += 1
                continue
            if token == "*":
                num1 = stack.pop()
                num2 = stack.pop()
                stack.append(num1*num2)
                i += 1
                continue
            if token == "/":
                num1 = stack.pop()
                num2 = stack.pop()
                if num1*num2>0:
                    stack.append(num2//num1)
                else:
                    # print num2, num1
                    # print abs(num2)//abs(num1), -(abs(num2)//abs(num1))
                    stack.append(-(abs(num2)//abs(num1)))
                i += 1
                continue
            else:
                stack.append(int(token))
                i += 1
                continue
            
        return stack[0]
            
            
