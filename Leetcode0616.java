class Solution {
    public String addBoldTag(String s, String[] dict) {
        //corner cases
        if (dict.length == 0 || s == null ||s.length()==0){
            return s;
        }
        
        // find every occuring interval for each word in dict in s and put them into a. arraylist
        ArrayList<int[]> intervals = new ArrayList<>();
        for(int i = 0; i<dict.length; i++){
            String word = dict[i];
            int index = s.indexOf(word);
            while(index != -1){
                int[] interval = {index, index+word.length()-1};
                intervals.add(interval);
                index = s.indexOf(word, index+1);
            };
        }
        if (intervals.size()==0){
            return s;
        }
        Collections.sort(intervals, new Comparator<int[]>(){public int compare(int[] a, int[] b) {return a[0] - b[0];}});
        // for (int i= 0; i<intervals.size(); i++){
        //     System.out.print(intervals.get(i)[0]);
        //     System.out.print(intervals.get(i)[1]);
        //     System.out.print("\n");
        // }
        // merge the intervals
        ArrayList<int[]> merged = new ArrayList<>();
        merged.add(intervals.get(0));
        for(int i = 1;i<intervals.size();i++){
            int[] currInterval = intervals.get(i);
            int [] prevInterval = merged.get(merged.size()-1);
            if (currInterval[0]<=prevInterval[1]+1){
                // we need to merge these two intervals
                prevInterval[1] = Math.max(prevInterval[1], currInterval[1]);
            }
            else{
                // No need to merge
                merged.add(currInterval);
            }                 
        }
        for (int i= 0; i<merged.size(); i++){
            System.out.print(merged.get(i)[0]);
            System.out.print(merged.get(i)[1]);
            System.out.print("\n");
        }
    
        String res = "";
        int i = 0, j = 0;
        while(i<s.length()){
            if (j>=merged.size()){
                res += s.charAt(i);
                i += 1;
                continue;
            }
            int start = merged.get(j)[0];
            int end = merged.get(j)[1];
            if (i<start){
                res += s.charAt(i);
                i += 1;
                continue;
            }
            else{
                //first add a <b>
                res += "<b>"+s.substring(i, end+1)+"</b>";
                i = end+1;
                j += 1;
            }
        }
    return res;
    }
}