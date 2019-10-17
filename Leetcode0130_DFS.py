class Solution(object):
    def dfs(self, i, j, board):
        if board[i][j] in ["$", "X"]:
            return 
        board[i][j] = "$"
        # traverse its neighbors
        if i-1>=0 and board[i-1][j] == "O":
            self.dfs(i-1, j, board)
        if i+1<len(board) and board[i+1][j] == "O":
            self.dfs(i+1, j, board)
        if j-1>=0 and board[i][j-1] == "O":
            self.dfs(i, j-1, board)
        if j+1<len(board[0]) and board[i][j+1] == "O":
            self.dfs(i, j+1, board)
            
            
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        # all "o"s that are reachable by "o"s on the boundary are nonflippable
        # we just need to do DFS/BFS from those nodes and find all nonflippable nodes
        # the flip the nodes that are flippable
        # THIS IS A BFS IMPLEMENTATION
        if not board or not board[0]:
            # no modification needs to be done
            return board
        if min(len(board), len(board[0])) <= 2:
            # no modification needs to be done
            return board
        queue = collections.deque()
        # scan the first and last row
        for j in range(len(board[0])):
            if board[0][j] == "O":
                self.dfs(0, j, board)
            if board[len(board)-1][j] == "O":
                self.dfs(len(board)-1, j, board)
        # scan the first and last column, skip the first and last element
        for i in range(1,len(board)-1):
            if board[i][0] == "O":
                self.dfs(i, 0, board)
            if board[i][len(board[0])-1] == "O":
                self.dfs(i, len(board[0])-1, board)
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == "O":
                    board[i][j] = "X"
                if board[i][j] == "$":
                    board[i][j] = "O"
        
