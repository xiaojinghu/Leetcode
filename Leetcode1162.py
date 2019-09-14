class Solution(object):       
    def maxDistance(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if not grid or not grid[0]:
            return -1
        visited = set()
        queue = collections.deque()
        maxLen = float('-inf')
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    queue.appendleft((i,j,0))
        if not queue or len(queue)==len(grid)*len(grid[0]):
            return -1
        
        while(queue):
            size = len(queue)
            for i in range(size):
                row, col, dist = queue.pop()
                if (row, col) in visited:
                    continue
                visited.add((row, col))
                maxLen = max(maxLen, dist)
                for (m,n) in [(row-1, col), (row, col-1), (row+1, col), (row, col+1)]:
                    if 0<=m<len(grid) and 0<=n<len(grid[0]) and grid[m][n]==0 and (m,n) not in visited:
                        queue.appendleft((m,n, dist+1))
                        
        return maxLen