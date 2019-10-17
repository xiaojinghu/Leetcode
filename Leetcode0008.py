class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        res = 0
        sign = 1
        i = 0
        if not str:
            return 0
        # discard the white spaces before the first char
        while(i<len(str) and str[i] == ' '):
            i += 1
        # if the whole str is composed of spaces
        if i>=len(str):
            return 0
        if str[i] not in '+-' and not str[i].isdigit():
            return 0
        
        if str[i] == '-':
            sign = -1
            i += 1
        else:
            if str[i] == '+':
                i += 1
        # we find the digit
        while(i<len(str)):
            if not str[i].isdigit():
                break
            # print i,str[i]
            res = res*10+int(str[i])
            # print res
            # determine if res overflows
            if sign == -1 and res>2**31:
                return -2147483648
            if sign == 1 and res>2**31-1:
                return 2147483647
            i += 1
        return res*sign
