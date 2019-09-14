class Solution(object):
    def isValid(self, s):
        left = 0
        right = 0
        for i in range(len(s)):
            if s[i] == "(":
                left += 1
            if s[i] == ')':
                right += 1
            if right>left:
                return False
        return left == right
    
    def removeInvalidParentheses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        # THIS IS A BFS IMPLEMENTATION
        #idea: view each tranformed (delete one "(" or ")") as the neighbour of the original string and check its validity 
        res = []
        visited = set()
        maxLen = float('-inf')
        queue = collections.deque([s])
        while(queue):
            currString = queue.pop()
            if currString in visited:
                continue
            visited.add(currString)
            # we check if the currString is valid
            if self.isValid(currString):
                # if currentString is valid, there is no need to add its neighbours because they will all be shorter
                if len(currString)<maxLen:
                    break
                res.append(currString)
                maxLen = len(currString)
                continue
            # we add the neighbours of the currString
            for i in range(len(currString)):
                if currString[i] in "()":
                    queue.appendleft(currString[:i]+currString[i+1:])
            # print queue
                
        return res