class Solution(object):
    def maxKilledEnemies(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        # This is a brutal force implementation
        maximum = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]=='0':
                    #search row i to the right
                    count = 0
                    for k in range(j+1, len(grid[0])):
                        if grid[i][k]=="0":
                            continue
                        if grid[i][k]=="E":
                            count += 1
                            continue
                        if grid[i][k]=="W":
                            break
                    # search row i to the left
                    for k in range(j-1, -1, -1):
                        if grid[i][k]=="0":
                            continue
                        if grid[i][k]=="E":
                            count += 1
                            continue
                        if grid[i][k]=="W":
                            break
                    # search column j downward
                    for k in range(i+1, len(grid)):
                        if grid[k][j]=="0":
                            continue
                        if grid[k][j]=="E":
                            count += 1
                            continue
                        if grid[k][j]=="W":
                            break
                    # serach column j upward
                    for k in range(i-1, -1, -1):
                        if grid[k][j]=="0":
                            continue
                        if grid[k][j]=="E":
                            count += 1
                            continue
                        if grid[k][j]=="W":
                            break
                            
                    maximum = max(maximum, count)
            
        return maximum
                    
