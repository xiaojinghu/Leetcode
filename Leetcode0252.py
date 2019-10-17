class Solution(object):
    def canAttendMeetings(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: bool
        """
        # THIS IS THE SORTING SOLUTION
        if not intervals:
            return True
        intervals.sort()
        endTime = intervals[0][1]
        
        for i in range(1, len(intervals)):
            # check if each meeting starts before the endtime of the fommer meeting
            if intervals[i][0]<endTime:
                return False
            # update end time
            endTime = intervals[i][1]
            i += 1
        return True
