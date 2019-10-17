import heapq
class Solution(object):   
    # This is a min heap implementation 
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        if not nums:
            return []
        
        # build a minheap to store the k largest numbers 
        heap = []
        heapq.heapify(heap)
        for num in nums:
            if len(heap)<k:
                heapq.heappush(heap, num)
                continue
            if num>heap[0]:
                heapq.heappop(heap)
                heapq.heappush(heap, num)
                
        return heapq.heappop(heap)
