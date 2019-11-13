class Solution {
    public String convert(String s, int numRows) {
        // corner cases
        if (numRows == 1){
            return s;
        }
        if (numRows == 2){
            String firstLine = "";
            String secondLine = "";
            for(int i=0;i<s.length();i++){
                if (i%2==0){
                    firstLine += s.charAt(i);
                }
                else{
                    secondLine += s.charAt(i);
                }
            }
            String res = firstLine + secondLine;
            return res;
        }
        
        // we group the string s in in blocks
        int blockSize = 2*numRows-2;
        String[] rows = new String[numRows];
        for (int i=0; i< numRows; i++){
            rows[i] = "";
        }
        //traverse through the string to decide which line the char belongs to.
        for(int i = 0; i<s.length();i++){
            int offset = i%blockSize;
            if (offset<=numRows-1){
                int row = offset;
                rows[row] += s.charAt(i);
            }
            else{
                // the distance from the last row
                int dist = offset-(numRows-1);
                rows[numRows-1-dist] += s.charAt(i);
            }
        }
        String res = "";
        for (int i=0; i<numRows; i++){
            // System.out.print(rows[i]+'\n');
            res += rows[i];
        }
        return res;
    }
}