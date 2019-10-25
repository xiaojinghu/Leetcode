class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        i = 0
        j = 0  
        while(i<len(s) and j<len(t)):
            # check if t[j] == s[i]
            if s[i] == t[j]:
                i += 1
                j += 1
             
                continue
            j += 1
        return i == len(s)