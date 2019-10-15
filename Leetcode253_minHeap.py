import heapq
class Solution(object):
    def minMeetingRooms(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        # sort all the intervals by starting time
        intervals.sort()
        roomNum = 0
        
        # store all the on going meetings in a heap
        minHeap = []
        heapq.heapify(minHeap)
        
        for i in range(len(intervals)):
            startTime, endTime = intervals[i]
            if not minHeap or startTime<minHeap[0]:
                # we need to assign a new room for this meeting
                roomNum += 1
                heapq.heappush(minHeap, endTime)
                continue
            # end current meeting
            heapq.heappop(minHeap)
            heapq.heappush(minHeap, endTime)
        return roomNum