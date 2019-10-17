import heapq
import collections
class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        # this is a max heap implementation
        # build a map to store the number and its count
        count = collections.Counter(nums)
        # build a minHeap
        minHeap = []
        heapq.heapify(minHeap)
        for num in count.keys():
            if len(minHeap)<k:
                heapq.heappush(minHeap, (count[num], num))
                continue
            if count[num]>minHeap[0][0]:
                heapq.heappop(minHeap)
                heapq.heappush(minHeap, (count[num], num))
        return [x[1] for x in minHeap]
                
        
                    
