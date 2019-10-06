class Solution(object):
    def dfs(self, grid, i, j, gold,visited):
        if (i, j) in visited:
            return gold
        visited.add((i,j))
        if i>=len(grid) or i<0 or j>=len(grid[0]) or j<0:
            return gold
        if grid[i][j] == 0:
            return gold
        gold += grid[i][j]
        # visited.add((i,j))
        maxSub = 0
        for m,n in [(i-1,j),(i,j+1), (i+1, j), (i, j-1)]:
            maxSub = max(maxSub,self.dfs(grid,m,n,gold,visited))
        visited.remove((i,j))
        gold -= grid[i][j]
        return maxSub
            
        
    def getMaximumGold(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        maxGold = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] != 0:
                    maxGold = max(maxGold, self.dfs(grid,i,j,0,set()))
        return maxGold
        