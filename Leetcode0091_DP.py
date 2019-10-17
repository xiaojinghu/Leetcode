class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        # dp1[i] means if we decode this decoding this number singly
        dp1 = [0]*len(s)
        # dp2[i] means if we decode this number with the former one
        dp2 = [0]*len(s)
        # Initialization
        if int(s[0])>0:
            dp1[0] = 1
        else:
            dp1[0] = 0
        dp2[0] = 0
        
        for i in range(1,len(s)):
            if int(s[i])>0:
                dp1[i] = dp1[i-1] + dp2[i-1]
            else:
                dp1[i] = 0
            # we check if we can combine s[i] with s[i-1]
            if int(s[i-1]+s[i])>26:
                dp2[i] = 0
                continue
            else:
                dp2[i] = dp1[i-1]
                
        return dp1[len(s)-1]+dp2[len(s)-1]
