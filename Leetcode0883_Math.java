class Solution {
    public int projectionArea(int[][] grid) {
        if (grid==null||grid.length==0||grid[0].length==0){
            return 0;
        }
        // maxY is the maximum value along the y axis
        int[] maxY = new int[grid[0].length];
        // maxX is the maximum value along the x axis
        int[] maxX = new int[grid.length];
        int count = 0;
        for (int x=0;x<grid.length;x++){
            for(int y=0;y<grid[0].length;y++){
                maxY[y] = Math.max(maxY[y], grid[x][y]);
                maxX[x] = Math.max(maxX[x], grid[x][y]); 
                if (grid[x][y]>0){
                    count += 1;
                }
            }
        }
        return Arrays.stream(maxX).sum()+Arrays.stream(maxY).sum()+count;
    }
}