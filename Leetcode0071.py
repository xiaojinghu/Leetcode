clasclass Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        if not path:
            return ""
        # the first token must be "/"
        stack = ["/"]
        i = 1
        pathList = path.split('/')
        
        #starting from the second item
        for i in range(1, len(pathList)):
            if pathList[i] == '.':
                #stay the current path
                continue
            if  pathList[i]=="..":
                #level up
                if len(stack)>=2:
                    stack.pop()
                continue
            if not pathList[i]:
                #do nothing
                continue
            stack.append(pathList[i])
        return '/'+'/'.join(stack[1:])
        
