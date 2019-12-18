class Solution {
    public void dfs(int i, int j, char[][]board){
        if (i<0 || j<0 || i>=board.length || j>=board[0].length ||board[i][j] !='O'){
            return;
        }
        board[i][j] = '+';
        // visit its neighbors
        dfs(i-1, j, board);
        dfs(i+1, j, board);
        dfs(i, j-1, board);
        dfs(i, j+1, board);
        return;
    }
    public void solve(char[][] board) {
        if (board==null || board.length==0||board[0].length==0){
            return;
        }
        // for each 'O' on the boundries, we dfs it.
        for (int j=0; j<board[0].length;j++){
            if (board[0][j] == 'O'){
                dfs(0, j, board);
            }
            if (board[board.length-1][j]=='O'){
                dfs(board.length-1, j, board);
            }
        }
        for (int i=0; i<board.length;i++){
            if (board[i][0] == 'O'){
                dfs(i, 0, board);
            }
            if (board[i][board[0].length-1]=='O'){
                dfs(i, board[0].length-1, board);
            }
        }
        for (int i=0;i<board.length;i++){
            for (int j=0;j<board[0].length;j++){
                if (board[i][j] == 'O'){
                    board[i][j] = 'X';
                }
                if (board[i][j]=='+'){
                    board[i][j] = 'O';
                }
            }
        }
        return;
    }
}