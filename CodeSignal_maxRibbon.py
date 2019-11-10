class solution(slef, ribbons):
    def countParts(self, ribbons, size):
        count = 0
        for length in ribbons:
            count += length/size
        return count

    def maxRibbon(self, ribbons, k):
        left = 1
        right = max(ribbons)+1

        while(left+1<right):
            middle = (left+right)/2
            currCount = self.countParts(ribbons, middle) 
            if currCount>=k:
                end = middle
            else:
                start == middle

        # check start
        if self.countParts(ribbons, start) >= k:
            return start

        return end

        
