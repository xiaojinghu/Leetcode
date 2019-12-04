class Solution(object):
    def maxAreaRectangle(self, heights):
        heights = [0]+heights+[0]
        stack = []
        maxArea = 0
        for i in range(len(heights)):
            if not stack or heights[i]>=heights[stack[-1]]:
                stack.append(i)
                continue
            while(heights[stack[-1]]>heights[i]):
                currHeight = heights[stack[-1]]
                stack.pop()
                maxArea = max(maxArea, currHeight*(i-stack[-1]-1))
                # print currHeight*(i-stack[-1]-1)
            stack.append(i)
        return maxArea
            
    def maximalRectangle(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        # 此题是之前那道的 Largest Rectangle in Histogram 的扩展，这道题的二维矩阵每一层向上都可以看做一个直方图，输入矩阵有多少行，就可以形成多少个直方图，对每个直方图都调用 Largest Rectangle in Histogram 中的方法，就可以得到最大的矩形面积。那么这道题唯一要做的就是将每一层都当作直方图的底层，并向上构造整个直方图.
        if not matrix or not matrix[0]:
            return 0
        matrix[0] = map(int, matrix[0])
        maxArea = self.maxAreaRectangle(matrix[0])
        for i in range(1, len(matrix)):
            matrix[i] = map(int, matrix[i])
            for j in range(len(matrix[i])):
                if matrix[i][j] == 1:
                    matrix[i][j] += matrix[i-1][j]
            currArea =self.maxAreaRectangle(matrix[i])
            maxArea = max(maxArea, currArea)
        return maxArea
                
        
        