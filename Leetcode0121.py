class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices:
            return 0
        minList = [prices[0]]*len(prices)
        maxList = [prices[-1]]*len(prices)
        maxProfit = 0
        for i in range(1, len(prices)):
            if prices[i]<minList[i-1]:
                minList[i] = prices[i]
            else:
                minList[i] = minList[i-1]
        for i in range(len(prices)-2, -1, -1):
            if prices[i]>maxList[i+1]:
                maxList[i] = prices[i]
            else:
                maxList[i] = prices[i+1]
        
        for i in range(len(minList)):
            maxProfit = max(maxProfit, maxList[i]-minList[i])
        return maxProfit