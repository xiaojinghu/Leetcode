class Solution(object):
    def integerBreak(self, n):
        """
        :type n: int
        :rtype: int
        """
        # Look For The Pattern
        # 2 = 1+1
        # 3 = 2+1
        # 4 = 2+2
        # 5 = 2+3
        # 6 = 3+3
        # 7 = 3+4
        # 8 = 3+3+2
        # 9 = 3+3+3
        # 10 = 3+3+4
        # we can see that we always try to split a number into 3s if we have a 4 or 1. (we cannot split a 4 into 3 and 1, we should split it into 2 and 2)
        if (n == 2 or n == 3):
            return n - 1
        res = 1;
        while (n > 4):
            res *= 3
            n -= 3
        return res * n