class Solution {
    public int findClosestStart(int[][] intervals, int target){
        int start = 0;
        int end = intervals.length-1;
        while(start+1<end){
            int middle = (start+end)/2;
            if (intervals[middle][0]>=target){
                end = middle;
            }
            else{
                start = middle;
            }
        }
        //check start and end
        if (intervals[start][0]>=target){
            return start;
        }
        if (intervals[end][0]>=target){
            return end;
        }
        return -1;
    } 
    
    
    public int[] findRightInterval(int[][] intervals) {
        int[] res = new int[intervals.length];
        //since there is no duplicate start, we can map start to its index
        HashMap<Integer, Integer> startToIndex = new HashMap<Integer, Integer>();
        for(int i=0;i<intervals.length;i++){
            startToIndex.put(intervals[i][0], i);
        };
        // sort intervals
        Arrays.sort(intervals, (a,b)->Integer.compare(a[0],b[0]));
        for(int i=0;i<intervals.length;i++){
            //check if there is a bigger start on the right side of the current interval
            int startIndex = findClosestStart(intervals, intervals[i][1]);
            if (startIndex == -1){
                // Not found
                res[startToIndex.get(intervals[i][0])] = -1;
            }
            else{
                res[startToIndex.get(intervals[i][0])] = startToIndex.get(intervals[startIndex][0]);
            }
        }
        return res;  
    }
}