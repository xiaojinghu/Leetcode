class Solution:
    def depthSum(self, nestedList):
        """
        :type nestedList: List[NestedInteger]
        :rtype: int
        """

        res = 0
        queue = collections.deque()
        level = 1
        for nList in nestedList:
            queue.appendleft((nList, level))
        while(queue):
            currList, currLevel = queue.pop()
            if currList.isInteger():
                res += currLevel*currList.getInteger()
                continue
            for child in currList.getList():
                queue.appendleft((child, currLevel+1))
        return res