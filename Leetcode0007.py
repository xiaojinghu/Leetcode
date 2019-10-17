class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        
        # cases:
        # 1.x ends with 0
        # 2.reverse(x) overflows
        
        # get the sign
        sign = 1 if x>=0 else -1
        
        res, x = 0, abs(x)
        
        while(x):
            res = res*10+x%10
            x = x/10
            
        # determine if the result overflows
        if sign == 1 and res>2**31-1:
            return 0
        if sign == -1 and res>2**31:
            return 0
        return res*sign
