class Solution(object):
    def updateBoard(self, board, click):
        """
        :type board: List[List[str]]
        :type click: List[int]
        :rtype: List[List[str]]
        """
        # idea: only when we are sure that the neighbor of the current pos is not 
        # a bomb do we reveal it
        queue = collections.deque()
        queue.appendleft(click)
        while(queue):
            i, j = queue.pop()
            # visited.add(i,j)
            if board[i][j] == "M":
                #change it to X, game over
                board[i][j] = "X"
                break
            if board[i][j] == "B" or board[i][j].isdigit():
                # this position has been revealed
                continue
            if board[i][j] == "E":
                # we need to reveal this position 
                countMine = 0
                for (m,n) in [(i-1,j-1),(i-1, j), (i-1, j+1), (i, j-1), (i, j+1), (i+1, j-1), (i+1, j), (i+1, j+1)]:
                    if 0<=m<len(board) and 0<=n<len(board[0]):
                        if board[m][n] == "M":
                            countMine +=  1
                if not countMine:
                    # This means there is no bomb around current Mine
                    board[i][j] = "B"
                    # we can continue to reveal its unrealed neighbors
                    for (m,n) in [(i-1,j-1),(i-1, j), (i-1, j+1), (i, j-1), (i, j+1), (i+1, j-1), (i+1, j), (i+1, j+1)]:
                        if 0<=m<len(board) and 0<=n<len(board[0]) and board[m][n] == "E":
                            queue.appendleft([m,n])
                else:
                    # there is bomb near it
                    board[i][j] = str(countMine)
        return board
                
                    
                        
            
        
