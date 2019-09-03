class Solution(object):
    def check(self, k, j, board):
        # check if k-th queen can be put in column j
        for i in range(len(board)):
            pos_i = board[i]
            # if they are at the same column
            if j == pos_i:
                return False
            # if they are at the same diagonal
            if abs(i-k) == abs(j-pos_i):
                return False
        return True
            
    def dfs(self, n, board, res):
        # the path stores the positions of the current queens
        # termination condition
        if len(board) == n:
            result = ["."*n for i in range(n)]
            for i in range(n):
                j = board[i]
                result[i] = result[i][:j]+"Q"+result[i][j+1:]
            res.append(result)
        for j in range(n):
            # if the current position is valid, we find the position of the next queen
            if self.check(len(board), j, board):
                self.dfs(n, board+[j], res)