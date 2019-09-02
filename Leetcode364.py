class Solution(object):
    def depthSumInverse(self, nestedList):
        """
        :type nestedList: List[NestedInteger]
        :rtype: int
        """
        if not nestedList:
            return 0
        
        # initialize two variables, weighted and unweighted
        weightedSum = 0
        unweightedSum = 0
        # nextLevel is a list to store items  which are not integer researved to be calculated in the next level
        nextLevel = []
        while(nestedList):
            # nestedList is a list that all items inside is nestInteger object
            nextLevel = []
            for item in nestedList:
                # if this item is an integer, we calculate its value in this level and add it the the unweightedSum
                if item.isInteger():
                    unweightedSum += item.getInteger()
                else:
                    nextLevel.extend(item.getList())
            nestedList = nextLevel
            weightedSum = weightedSum + unweightedSum
            print weightedSum
        return weightedSum
        