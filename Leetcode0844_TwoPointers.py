class Solution(object):
    def backspaceCompare(self, s, t):
        """
        :type S: str
        :type T: str
        :rtype: bool
        """
        #idea: start comparison backwords using pointers
        i = len(s)-1
        j = len(t)-1
        # count1, count2 means how many "#" there are in s and t seperately.
        count1 = 0
        count2 = 0
        
        while(i>=0 and j>=0):
            if s[i] == '#':
                count1 += 1
                i -= 1
                continue
            
            if t[j] == '#':
                count2 += 1
                j -= 1
                continue
                
            # now s[i] and s[j] are both letters
            # we need to check if they are letters that need to be deleted
            if count1>0:
                i -= 1
                count1 -= 1
                continue
            if count2>0:
                j -= 1
                count2 -= 1
                continue
            # compare s[i] and t[j]

            if s[i]!=t[j]:
                return False
            i -= 1
            j -= 1
        # now there should be no valid letters in both s and t
        while(i>=0):
            if s[i] == "#":
                i -= 1
                count1 += 1
                continue
            if count1>0:
                count1 -= 0
                i -= 1
                continue
            return False
        
        while(j>=0):
            if t[j] == "#" :
                j -= 1
                count2 += 1
                continue
            if count2>0:
                count2 -= 1
                j -= 1
                continue
            return False
        return True