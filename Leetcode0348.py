class TicTacToe(object):
    def __init__(self, n):
        """
        Initialize your data structure here.
        :type n: int
        """
        self.n = n
        self.rowCountX = [0]*n
        self.colCountX = [0]*n
        self.rowCountO = [0]*n
        self.colCountO = [0]*n
        self.diagnalCountX = [0]*2
        self.diagnalCountO = [0]*2
     

    def move(self, row, col, player):
        """
        Player {player} makes a move at ({row}, {col}).
        @param row The row of the board.
        @param col The column of the board.
        @param player The player, can be either 1 or 2.
        @return The current winning condition, can be either:
                0: No one wins.
                1: Player 1 wins.
                2: Player 2 wins.
        :type row: int
        :type col: int
        :type player: int
        :rtype: int
        """
        if player == 1:
            rowCount = self.rowCountX
            colCount = self.colCountX
            diagnalCount = self.diagnalCountX
        else:
            rowCount = self.rowCountO
            colCount = self.colCountO
            diagnalCount = self.diagnalCountO
            
        # update and check row
        rowCount[row] += 1
        if rowCount[row] == self.n:
            return player
        # update and check col
        colCount[col] += 1
        if colCount[col] == self.n:
            return player
        # check left diagnal
        if row == col :
            diagnalCount[0] += 1
            if diagnalCount[0] == self.n:
                return player
        # check right diagnal
        if row+col ==self.n-1:
            diagnalCount[1] += 1
            if diagnalCount[1] == self.n:
                return player
        
        # a draw
        return 0
            
        
        


# Your TicTacToe object will be instantiated and called as such:
# obj = TicTacToe(n)
# param_1 = obj.move(row,col,player)