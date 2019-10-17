class Solution(object):
               
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        
        if not grid or not grid[0]:
            return 0        
        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                queue = collections.deque()
                if grid[i][j] == "1":
                    queue.appendleft((i,j))
                    count += 1
                if not queue:
                    continue
                while(queue):
                    m, n = queue.pop()
                    if grid[m][n] == "V":
                        continue   
                    # if this node is water, we do nothing
                    if grid[m][n] == "0":
                        grid[m][n] = "V"
                        continue
                    grid[m][n] = "V"
                    # visit its neighbors
                    if m-1>=0 and grid[m-1][n] == "1":
                        queue.appendleft((m-1, n))
                    if m+1<len(grid) and grid[m+1][n] == "1":
                        queue.appendleft((m+1, n))
                    if n-1>=0 and grid[m][n-1] == "1":
                        queue.appendleft((m, n-1))
                    if n+1<len(grid[0]) and grid[m][n+1]=="1":
                        queue.appendleft((m, n+1))
                    # print m,n, queue
                # print grid
        return count
                  
