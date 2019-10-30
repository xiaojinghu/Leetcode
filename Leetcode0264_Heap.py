import heapq
class Solution(object):
    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1:
            return 1
        
        minHeap = [2,3,5]
        count = 1 
        prev = 1
        while(count<n):
            res = heapq.heappop(minHeap)
            # skip duplicate
            if res == prev:
                prev = res
                continue
            heapq.heappush(minHeap, res*2)
            heapq.heappush(minHeap, res*3)
            heapq.heappush(minHeap, res*5)
            prev = res
            count += 1

        return res
            