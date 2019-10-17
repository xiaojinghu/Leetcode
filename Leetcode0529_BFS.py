class Solution(object):
    def bfs(self, i, j, board):
        # termination
        # we meet a "bomb"
        if board[i][j] == "M":
            return
        # i, j has already been visited
        if board[i][j] == "B" or board[i][j].isdigit():
            return 
        # now i, j is an unrevealed empty space, we count how many mines is near it
        count = 0
        for row, col in [(i-1, j-1), (i-1, j), (i-1, j+1), (i, j-1), (i, j+1), (i+1, j-1), (i+1, j), (i+1, j+1)]:
           
            if row>=0 and row<len(board) and col>=0 and col<(len(board[0])):
                if board[row][col] in "MX":
                    count += 1      
        if board[i][j] != "B":
            if count == 0:
                board[i][j] = "B"
            else:
                board[i][j] = str(count)
        if board[i][j] == "B":
            for row, col in [(i-1, j-1), (i-1, j), (i-1, j+1), (i, j-1), (i, j+1), (i+1, j-1), (i+1, j), (i+1, j+1)]:
                if row>=0 and row<len(board) and col>=0 and col<(len(board[0])) and board[row][col] == "E":
                    self.bfs(row, col, board)
               
    def updateBoard(self, board, click):
        """
        :type board: List[List[str]]
        :type click: List[int]
        :rtype: List[List[str]]
        """
        # THIS IS A DFS IMPLEMENTATION
        row, col = click
        if board[row][col] == "M":
            board[row][col] = "X"
            return board
        if board[row][col] == "E":
            self.bfs(row, col, board)
        return board
