class Solution(object):
    
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        if not s:
            return s
        
        stack = []
        i = 0
        while(i<len(s)):
            # print i, stack
            if s[i].isdigit():
                # we get the complete number
                num = ""
                while(i<len(s) and s[i].isdigit()):
                    num += s[i]
                    i += 1
                # we push the number into the stack
                stack.append(num)
                continue
            if s[i] == '[':
                stack.append(s[i])
                i += 1
                continue
            if s[i].isalpha():
                # we get the complete string
                string = ''
                while(i<len(s) and s[i].isalpha()):
                    string += s[i]
                    i += 1
                stack.append(string)
                continue
            if s[i]==']':
                # it means we find a substructure of X[abc...]
                string  = ''
                while(stack[-1]!='['):
                    string = stack.pop()+string
                # pop the '['
                stack.pop()
                # pop the number
                num = int(stack.pop())
                stack.append(num*string)
                i += 1
                continue
        res = ''
        for string in stack:
            res += string
        return res