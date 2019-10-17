                if grid[i][j] == '0':
                    dpRight[i][j] = dpRight[i][j+1]
                if grid[i][j] == 'E':
                    dpRight[i][j] = dpRight[i][j+1]+1
                if grid[i][j] =="W":
                    dpRight[i][j] = 0
                continue
          
        # Third the downward direction
        dpDown = [[0]*len(grid[0]) for i in range(len(grid))]
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if i == 0:
                    if grid[i][j]=="E":
                        dpDown[i][j] = 1
                    else:
                        dpDown[i][j] = 0
                    continue
                    
                if grid[i][j] == '0':
                    dpDown[i][j] = dpDown[i-1][j]
                if grid[i][j] == 'E':
                    dpDown[i][j] = dpDown[i-1][j]+1
                if grid[i][j] =="W":
                    dpDown[i][j] = 0
                continue
        
        # Fourth, the upward direction
        dpUp = [[0]*len(grid[0]) for i in range(len(grid))]
        for i in range(len(grid)-1, -1, -1):
            for j in range(len(grid[0])):
                if i == len(grid)-1:
                    if grid[i][j] == "E":
                        dpUp[i][j] = 1
                    else:
                        dpUp[i][j] = 0
                    continue
                
                if grid[i][j] == '0':
                    dpUp[i][j] = dpUp[i+1][j]
                if grid[i][j] == 'E':
                    dpUp[i][j] = dpUp[i+1][j]+1
                if grid[i][j] =="W":
                    dpUp[i][j] = 0
                continue
                
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "0":
                    maximum = max(maximum, dpLeft[i][j]+dpRight[i][j]+dpUp[i][j]+dpDown[i][j])

        return maximum
