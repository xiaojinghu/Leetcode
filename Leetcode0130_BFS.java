import java.awt.Point;
class Solution {
    public void solve(char[][] board) {
        if (board == null || board.length==0 || board[0] == null){
            return;
        }
        int rowNum = board.length;
        int colNum = board[0].length;
        // System.out.println(rowNum);
        // System.out.println(colNum);
        Queue<Point> queue = new LinkedList<Point>();
        for(int j=0;j<colNum; j++){
            if (board[0][j]=='O'){
                queue.offer(new Point(0,j));
            }
            if (board[rowNum-1][j]=='O'){
                queue.offer(new Point(rowNum-1, j));
            }
        }
        for (int i=0; i<rowNum; i++){
            if (board[i][0]=='O'){
                queue.offer(new Point(i,0));
            }
            if (board[i][colNum-1]=='O'){
                queue.offer(new Point(i, colNum-1));
            }
        }
        while(!queue.isEmpty()){
            Point currNode = queue.poll();
            int i = currNode.x;
            int j = currNode.y;
            if (board[i][j] == 'O'){
                board[i][j] = '+';
                // visit its neighbors
                if (i-1>=0 && board[i-1][j] == 'O'){
                    queue.offer(new Point(i-1, j));
                }
                if (i+1<rowNum && board[i+1][j]=='O'){
                    queue.offer(new Point(i+1, j));
                }
                if (j-1>=0 && board[i][j-1]=='O'){
                    queue.offer(new Point(i,j-1));
                }
                if (j+1<colNum && board[i][j+1]=='O'){
                    queue.offer(new Point(i, j+1));
                }
            }
            
        }
        
        // scan board to flip all 'O' to 'X' and convert
        // '+' back to 'O'
        for (int i=0;i<rowNum;i++){
            for(int j=0;j<colNum;j++){
                if (board[i][j] == 'O'){
                    board[i][j] = 'X';
                }
                if (board[i][j] == '+'){
                    board[i][j] = 'O';
                }
            }
        }
        return ;
    }
}