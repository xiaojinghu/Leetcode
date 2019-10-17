def nest_sum(depth, nestedList, sum_):
    if nestedList.isInteger():
        return sum_ + nestedList.getInteger() * depth
    temp = 0
    for item in nestedList.getList():
        temp += nest_sum(depth + 1, item, sum_)       
    return sum_ + temp


class Solution:
    def depthSum(self, nestedList):
        """
        :type nestedList: List[NestedInteger]
        :rtype: int
        """
        # print(type(nestedList[0]))
        res = 0
        for item in nestedList:
            depth = 1
            sum_ = 0
            res += nest_sum(depth, item, sum_) 
        return res
