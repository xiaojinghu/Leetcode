class Solution(object):
    def minCost(self, costs):
        """
        :type costs: List[List[int]]
        :rtype: int
        """
        if not costs:
            return 0
        if len(costs) == 1:
            return min(costs[0])
        
        # initialize the three DP variable      
        dpRed, dpBlue, dpGreen = costs[0]
        
        for i in range(1, len(costs)):
            newdpRed = min(dpBlue, dpGreen)+costs[i][0]
            newdpBlue = min(dpRed, dpGreen)+costs[i][1]
            newdpGreen = min(dpRed, dpBlue)+costs[i][2]
            dpRed, dpBlue, dpGreen = newdpRed, newdpBlue, newdpGreen
        return min(dpRed,dpBlue, dpGreen)