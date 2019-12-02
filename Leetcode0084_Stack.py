class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        # Basic idea: 对于每一个bar，向左右扩展，直到找到比它更低的bar或者边界。我们可以在heights左右加上0，这样对于每个bar,我们可以找到以此bar为高度的长方形的最大面积。但是此方法需要O(n^2)的复杂度。因此我们需要寻找一种时间复杂度更低的寻找一个bar左右边界的算法。在网上流传了一个设计极其巧妙的方法，借助一个stack可以将时间复杂度降为O(n)。
        # 这种算法的思想是维护一个递增的栈，这个栈保存了元素在数组中的位置。 这样在栈中每一个左边的bar都比本身小，所以左边就天然有界了，也就是左边界就是左边的一个bar。遍历一遍height数组，在将height数组入栈的时候，如果当前元素height[i]比栈顶元素小，则我们又找到了栈顶元素的右边界。因此我们在此时就可以计算以栈顶元素为最低bar的矩形面积了，因为左右边界我们都已经找到了，而且是在O(1)的时间复杂度内找到的。然后就可以将栈顶元素出栈了。这样每出栈一个元素，即计算以此元素为最低点的矩形面积。当最终栈空的时候我们就计算出了以所有bar为最低点的矩形面积。为保证让所有元素都出栈，我们在height数组最后加一个0，因为一个元素要出栈必须要遇到一个比他小的元素，也就是右边界。
        if not heights:
            return 0
        heights = [0]+heights+[0]
        # keep a monotonic stack
        stack = []
        maxArea = 0
        for i in range(len(heights)):
            currHeight = heights[i]
            # if the current height won't interrupt the monotonous stack, we push it into the stack
            if not stack or currHeight>=heights[stack[-1]]:
                stack.append(i)
                continue
            # the index of the right boundry is i, we need to find the left boundry
            while(stack and heights[stack[-1]]>currHeight):
                topHeight = heights[stack[-1]]
                stack.pop()
                #the index of the left boundry is stack[-1]
                currArea = topHeight*(i-stack[-1]-1)
                maxArea = max(maxArea, currArea)
            stack.append(i)
        return maxArea