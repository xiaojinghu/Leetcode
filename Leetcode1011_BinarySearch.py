class Solution(object):
    def check(self, weights, capacity, D):
        days = 0
        currWeight = 0
        for weight in weights:
            if currWeight + weight > capacity:
                days += 1
                currWeight = weight
                continue
            currWeight += weight
        if currWeight:
            days += 1
        return days<=D
            
    def shipWithinDays(self, weights, D):
        """
        :type weights: List[int]
        :type D: int
        :rtype: int
        """
        left = max(weights)
        right = sum(weights)
        
        while(left+1<right):
            middle = (left+right)/2
            if self.check(weights, middle, D):
                right = middle
            else:
                left = middle
        
        if self.check(weights, left, D):
            return left
        return right
        