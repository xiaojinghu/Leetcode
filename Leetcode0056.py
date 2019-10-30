class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        if not intervals:
            return []
        # first sort these intervals by starting time
        intervals.sort()
        res = []
        for i in range(len(intervals)):
            currInterval = intervals[i]
            if not res:
                res.append(currInterval)
                continue
            # we need to check if the current interval has intersection with the previous one
            prevInterval = res[-1]
            if currInterval[0]>prevInterval[1]:
                # no intersection, add current interval into
                # the result and move on
                res.append(currInterval)
                continue
            # current interval has intersection with the previous interval, and it can only has intersection with the one before, we merge it with the previous one and move on
            prevInterval[1] = max([currInterval[1], prevInterval[1]])
            
        return res