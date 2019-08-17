class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        if not path:
            return path
        if len(path) == 1:
            return path
        
        newPath = []
        result = ""
        pathList = path.split('/')
        # print pathList
        # The first item must be "/"
        # We push it into the stack
        newPath.append('/')
        # Starting from the second item
        for i in range(1, len(pathList)):
            if pathList[i] == ".":
                # stay the current path
                print newPath
                continue
            if pathList[i] == "..":
                # go one level up
                if len(newPath)>=2:
                    newPath.pop()
                print newPath
                continue
            if not pathList[i]:
                continue
            newPath.append(pathList[i]+'/')
            # print newPath

        for i in range(len(newPath)):
            result += newPath[i]
        # print result
        if len(newPath)==1:
            return result
        return result[:-1]
        