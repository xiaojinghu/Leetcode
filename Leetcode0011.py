class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        if not height or len(height)<=1:
            return 0
        maxArea = 0
        i = 0
        j = len(height)-1
        
        while(i<j):
            # the height of the container is determined
            # by the minimun height of i and j
            currHeight = min(height[i], height[j])
            # currArea is the largest area with currHeight since the distance between i and j is the biggest one
            currArea = currHeight*(j-i)
            maxArea = max(maxArea, currArea)
            if height[i]<=height[j]:
                # we move i farward to see if we can find a bigger area
                i += 1
            else:
                # we move j backward to see if we can fisn a bigger area
                j -= 1
        return maxArea