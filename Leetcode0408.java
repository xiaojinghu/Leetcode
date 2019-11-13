class Solution {
    public boolean validWordAbbreviation(String word, String abbr) {
        if (abbr.length()>word.length()){
            return false;
        }
        int prevI = -1, currI = 0, currJ = 0;
        int count = 0;
        while(currI<word.length() && currJ<abbr.length()){
            if (Character.isDigit(abbr.charAt(currJ))){
                // count cannot start with an zero
                if (count == 0 && abbr.charAt(currJ)=='0'){
                    return false;
                }
                count = (abbr.charAt(currJ)-'0') + count*10;
                currJ ++;
                continue;
            }
            else if (Character.isLetter(abbr.charAt(currJ))){
                if (count == 0){
                    if (abbr.charAt(currJ)!=word.charAt(currI)){
                        return false;
                    }
                    currI += 1;
                    currJ += 1;
                }
                else{
                    currI += count;
                    count = 0;
                }
            }
            else{
                return false;
            }
        }
        return currJ == abbr.length() && (currI+count)==word.length();
    }
    
}