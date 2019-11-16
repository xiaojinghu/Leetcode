class Solution {
    public int longestValidParentheses(String s) {
        //idea: traverse from left and right to find the maximum valid parentheses length
        if (s == null ||s.isEmpty()){
            return 0;
        }
        int left1 = 0, right1 = 0, left2 = 0, right2 = 0, maxLen = 0;
        for(int i=0;i<s.length();i++){
            char currCharLeft = s.charAt(i);
            char currCharRight = s.charAt(s.length()-1-i);
            //first check from the left
            if (currCharLeft=='('){
                left1 ++;
            }
            else{
                right1 ++;
                //check if we need to update the maximum length
                if (left1 == right1){
                    maxLen = Math.max(maxLen, 2*left1);
                }
                //check if we need to reset left and right
                if (right1>left1){
                    left1 = 0;
                    right1 = 0;
                }
            }
            //check from the right
            if (currCharRight == ')'){
                right2 ++;
            }
            else{
                left2 ++;
                // check if we need to update the maxLen
                if (left2==right2){
                     maxLen = Math.max(maxLen, 2*left2);
                }
                // check if we need to reset left2 and right2
                if (left2>right2){
                    left2 = 0;
                    right2 = 0;
                }
            }
        }
        return maxLen;
    }
}