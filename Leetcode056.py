class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        if not intervals:
            return []
        intervals.sort()
        res = []
        for i in range(len(intervals)):
            if not res:
                res.append(intervals[i])
                continue
            # we check if the current interval overlaps with the former merged one
            if intervals[i][0]>res[-1][1]:
                #No overlap 
                res.append(intervals[i])
                continue
            # we need to merge res[-1] and intervals[i]
            lastInterval = res.pop()
            res.append([lastInterval[0], max(lastInterval[1],intervals[i][1])])
        return res