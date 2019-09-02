class Solution(object):
    def dfs(self, i, j, grid):
        if i<0 or i>=len(grid):
            return 
        if j<0 or j>=len(grid[0]):
            return
        if grid[i][j]==0 or grid[i][j]=="V":
            return 
        grid[i][j]="V"
        if 0<=i-1<len(grid) and grid[i-1][j]=="1":
            self.dfs(i-1, j, grid)
        if 0<=i+1<len(grid) and grid[i+1][j]=="1":
            self.dfs(i+1, j, grid)
        if 0<=j-1<len(grid[0]) and grid[i][j-1]=="1":
            self.dfs(i, j-1, grid)
        if 0<=j+1<len(grid[0]) and grid[i][j+1]=="1":
            self.dfs(i, j+1, grid)
        return
        
              
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        
        if not grid:
            return 0
        
        m = len(grid)
        n = len(grid[0])
        
        count = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    self.dfs(i, j, grid)
                    count += 1
        return count
                   
                   