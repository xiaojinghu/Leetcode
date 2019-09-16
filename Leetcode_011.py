class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        maxWater = 0
        i = 0
        j = len(height)-1
        while(i<j):
            # we need to find the maximum water between i and j
            if height[i]<= height[j]:
                currWater = (j-i)*height[i]
                maxWater = max(maxWater, currWater)
                # currently the lower board is height[i] and we should move i forward to see if we can get a bigger area
                i += 1
                continue
            currWater = (j-i)*height[j]
            maxWater = max(maxWater, currWater)
            j -= 1
        return maxWater