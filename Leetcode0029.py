class Solution(object):
    
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        # first consider the situation of overflow
        # case 1
        if dividend < -2**31:
            return 2**31-1
        # case 2
        if dividend > 2**31-1:
            return 2**31-1
        #case 3
        if dividend == -2**31:
            if divisor == 1:
                return -2**31
            if divisor == -1:
                return 2**31-1
        #case 4 
        if divisor == 1:
            return dividend
        if divisor == -1:
            return -dividend
        
        # calculate the sign of the result
        if (dividend > 0 and divisor > 0) or (dividend<0 and divisor<0):
            sign = 1
        else:
            sign = -1
        # convert both divisor and divident to positive values
        divisor = abs(divisor)
        dividend = abs(dividend)
        
        quotient = 0
        i = 0
        # first find the maximum divisor 
        while(dividend>divisor):
            i += 1
            divisor = divisor<<1
        # now divisor>=divident
        # and divisor = oriDivisor * 2^i
        for j in range(i, -1, -1):
            if divisor<=dividend:
                quotient += (1<<j)
                dividend -= divisor
            divisor = divisor>>1
        return sign*quotient
        
