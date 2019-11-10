from collections import deque
class Solution(object):
    def closedIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        queue = deque()
        if len(grid)<=2 or len(grid[0])<=2:
            return 0
        # visited all 0s accessible by 0s on the boundary
        # two rows
        for i in range(len(grid)):
            if grid[i][0] == 0:
                queue.appendleft((i, 0))
            if grid[i][len(grid[0])-1] == 0:
                queue.appendleft((i, len(grid[0])-1))
        
        for j in range(len(grid[0])):
            if grid[0][j] == 0:
                queue.appendleft((0, j))
            if grid[len(grid)-1][j] == 0:
                queue.appendleft((len(grid)-1, j))
        # print queue    
        while(queue):
            i, j = queue.pop()
            if grid[i][j] == 1:
                continue
            grid[i][j] = 1
            for m, n in [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]:
                if 0<=m<len(grid) and 0<=n<len(grid[0]) and grid[m][n] == 0:
                    queue.appendleft((m,n))
        # print grid
        # count the remaining islands
        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    continue
                queue = deque([(i,j)])
                count += 1
                while(queue):
                    p, q = queue.pop()
                    if grid[p][q] == 1:
                        continue
                    grid[p][q] = 1
                    for m, n in [(p-1, q), (p+1, q), (p, q-1), (p, q+1)]:
                        if 0<=m<len(grid) and 0<=n<len(grid[0]) and grid[m][n] == 0:
                            queue.appendleft((m,n))
                            
        return count