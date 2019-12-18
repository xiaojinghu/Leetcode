import java.awt.Point;
class Solution {
    public int numIslands(char[][] grid) {
        if (grid==null||grid.length==0||grid[0].length==0){
            return 0;
        }
        int count = 0;
        for (int x=0;x<grid.length;x++){
            for (int y=0;y<grid[0].length;y++){
                if (grid[x][y] == '1'){
                    count += 1;
                    Queue<Point> queue = new LinkedList<Point>();
                    queue.offer(new Point(x,y));
                    while(!queue.isEmpty()){
                        Point currPoint = queue.poll();
                        int i = currPoint.x;
                        int j = currPoint.y;
                        if (grid[i][j] == '1'){
                            grid[i][j] = '0';
                           if (i-1>=0&&grid[i-1][j]=='1'){queue.offer(new Point(i-1, j));}
                           if (i+1<grid.length&&grid[i+1][j]=='1'){queue.offer(new Point(i+1, j));}
                           if (j-1>=0&&grid[i][j-1]=='1'){queue.offer(new Point(i, j-1));}
                           if (j+1<grid[0].length&&grid[i][j+1]=='1'){queue.offer(new Point(i, j+1));}
                       }
                   }
                }
            }
        }
        
        return count;
    }
}