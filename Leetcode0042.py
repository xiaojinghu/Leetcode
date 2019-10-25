class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        if not height or len(height)<=2:
            return 0
        
        water = 0
        # the height of water if index i is determined by min(max(height[:i]), max(height[i+1:]))
        
        # first find the maximum height from both sides
        leftMax = [height[0]]*len(height)
        rightMax = [height[-1]] * len(height)
        for i in range(1, len(height)-1):
            leftMax[i] = max(height[i], leftMax[i-1])
            j = len(height)-1-i
            rightMax[j] = max(height[j], rightMax[j+1])
        leftMax[-1] = max(height[-1], leftMax[-2])
        rightMax[0] = max(height[0], rightMax[1])
        # calculate the water depth for each index i
        for i in range(len(height)):
            currHeight = min(leftMax[i], rightMax[i])
            currDepth = currHeight-height[i]
            water += currDepth
        return water