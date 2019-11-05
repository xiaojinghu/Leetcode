class Solution(object):
    def calHour(self, k, piles):
        """
        calculate how many hours koko takes eating up all piles of bananas
        """
        hour = 0
        for count in piles:
            hour += count/k
            if count%k!=0:
                hour += 1
        return hour
    
    def minEatingSpeed(self, piles, H):
        """
        :type piles: List[int]
        :type H: int
        :rtype: int
        """
        if not piles:
            return 0
        left = 1
        right = max(piles)
        while(left+1<right):
            middle = (left+right)/2
            hour = self.calHour(middle, piles)
            if hour == H:
                right = middle
                continue
            if hour < H:
                right = middle
                continue
            if hour > H:
                left = middle
                continue
        # check left
        if self.calHour(left, piles)<=H:
            return left
        return right
            