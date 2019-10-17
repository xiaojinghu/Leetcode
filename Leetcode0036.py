class Solution(object):
    def isValidRow(self, board):
        for i in range(len(board)):
            Dict = set()
            for j in range(len(board[0])):
                if board[i][j] == '.':
                    continue
                if board[i][j] not in Dict:
                    Dict.add(board[i][j])
                    continue
                return False
        return True
    
    
    def isValidCol(self, board):
        for j in range(len(board[0])):
            Dict = set()
            for i in range(len(board)):
                if board[i][j] == '.':
                    continue
                if board[i][j] not in Dict:
                    Dict.add(board[i][j])
                    continue
                return False
        return True
    
    def isValidBox(self, board):
        for i in range(len(board)/3):
            for j in range(len(board[0])/3):
                Dict = set()
                for p in range(3):
                    for q in range(3): 
                        if board[3*i+p][3*j+q]== '.':
                            continue
                        if board[3*i+p][3*j+q] not in Dict:
                            Dict.add(board[3*i+p][3*j+q])
                            continue
                        # print i, j, board[i+p][j+q], Dict
                        return False
                
        return True
    
    
    
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        print self.isValidRow(board) 
        print self.isValidCol(board) 
        print self.isValidBox(board)
        return self.isValidRow(board) and self.isValidCol(board) and self.isValidBox(board)
