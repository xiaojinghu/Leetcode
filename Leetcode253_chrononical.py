class Solution(object):
    def minMeetingRooms(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        # chronological ordering
        # put all starting time in a stack
        start = [x[0] for x in intervals]
        # put all ending time in a stack
        end = [x[1] for x in intervals]
        # sort both starting time and ending time in ascending order
        start.sort()
        end.sort()
        
        # Initialize two pinters
        # Meetings before startPtr have already been allocated
        # Meetings before endPtr have already ended
        startPtr = 0
        endPtr = 0
        
        roomNum = 0
        # We keep allocating meetings util there is no meetings left
        while(startPtr<len(intervals)):
            # we check whether it starts after endPtr
            if start[startPtr]>=end[endPtr]:
                # end current meeting
                endPtr += 1
                # Since the current meeting has already ended
                # we can just reuse the old meeting rooms
                # allocate the next meeting
                startPtr += 1
                continue
            # this means that all the rooms opened now are in use, so we have to open another meeting room
            roomNum += 1
            startPtr += 1
        return roomNum