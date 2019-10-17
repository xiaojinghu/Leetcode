import heapq

class Solution(object):
    def minusCalDistance(self, point):
        x = point[0]
        y = point[1]
        distance = x**2+y**2
        return (-distance, x, y)
    
    def kClosest(self, points, K):
        """
        :type points: List[List[int]]
        :type K: int
        :rtype: List[List[int]]
        """
        if K==0 or not points:
            return []
        maxHeap = map(self.minusCalDistance, points[:K])
        heapq.heapify(maxHeap)
        for i in range(K, len(points)):
            point = self.minusCalDistance(points[i])
            if point[0]>maxHeap[0][0]:
                heapq.heappop(maxHeap)
                heapq.heappush(maxHeap, point)
        # print maxHeap
        results = [[y,z] for x,y,z in maxHeap]
        # print results
        # results = results[::-1]
        return results
        
