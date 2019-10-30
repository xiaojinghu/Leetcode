import heapq
class Solution(object):
    def minMeetingRooms(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        if not intervals:
            return 0
        
        roomNum = 1
        intervals.sort()
        
        # for each upcoming meeting, we neend only to compare its start time with the previous meeting which ends the earlist, we call it endFirst. If the current meeting starts before endFirst, we will need to open a new room, else can just reuse the rooms assigned before.
        minHeap = [intervals[0][1]]
        heapq.heapify(minHeap)
        for i in range(1, len(intervals)):
            startTime, endTime = intervals[i]
            if startTime>=minHeap[0]:
                # we end the previous meeting and start a new meeting. There is no need to spare a new room
                heapq.heappop(minHeap)
                heapq.heappush(minHeap, endTime)
                continue
            #b we neend to spare a new room
            roomNum += 1
            heapq.heappush(minHeap, endTime)
        return roomNum
