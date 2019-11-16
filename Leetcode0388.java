class Solution {
    // idea: first split the path according to '\n', and decide the level of each dirName based on the count of '\t'.
    // then when we meet a file name, suppose its level is i, then its parent dir is the last one that has level i-1.
    public int lengthLongestPath(String input) {
        if (input == null || input.isEmpty()){
            return 0;
        }
        int maxLen = 0;
        Map<Integer, ArrayList> levelToDirs = 
            new HashMap<Integer,ArrayList>();
        // split the input based on '\n'
        String[] dirs = input.split("\n");
        for (int i=0;i<dirs.length;i++){
            //when we arrive at a '/n' we know that the current directory has ended and the number of '/t' represents its level
            String currStr = dirs[i];
            // count the level of currStr
            int j = 0;
            while(currStr.charAt(j) == '\t'){
                j += 1;
            }
            int currLevel = j+1;
            String currDir = currStr.substring(j);
            //check if the current dir is a file
            boolean isFile =  false;
            if (currDir.indexOf('.')!=-1){
                isFile = true;
            }
            //check its parent dir
            if (currLevel>=2){
                ArrayList parentDirList = 
                    levelToDirs.get(currLevel-1);
                // System.out.println(parentDirList.get(parentDirList.size()-1).getClass().getName());
                String parentDir = (String)
                    parentDirList.get(parentDirList.size()-1);
                currDir = parentDir+'/'+currDir;
            }
            // update the maximum length
            // boolean isFile = true;
            if(isFile){
                maxLen = Math.max(maxLen, currDir.length());
            }
            // add the current dir to the hashMap
            if(!levelToDirs.containsKey(currLevel)){
                levelToDirs.put(currLevel, new 
                                ArrayList<String>());
            }
            levelToDirs.get(currLevel).add(currDir);
        }
        return maxLen;
    }
}