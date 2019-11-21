class Solution(object):
    def nextGreaterElement(self, n):
        """
        :type n: int
        :rtype: int
        """
        # 思路：看起来像是31的变种。将我们要找的整数记为sn
        # 1. 对于个位数，应返回-1；
        # 2. 对于多位数， 我们要找到最小的sn
        #    n=12345   sn = 1235(4)
        #    n=12354   sn = 124(35)
        #    ....
        #    process:
        #    a). find the first i from the back such that s[i]<s[i+1]
        #    b). find the last j from s[i+1:] such that s[j]>s[i]
        #    c). reverse s[j:]
        # 3. when we find sn, we need to check if it is a 32 bit value :)
        s = list(str(n))
        if len(s)<=1:
            return -1
        
        i = len(s)-2
        while(i>=0):
            if s[i]<s[i+1]:
                break
            i -= 1
        # check if i exists
        if i == -1:
            return -1
        j = len(s)-1
    
        while(j>i):
            if s[j]>s[i]:
                break
            j -= 1
        
        if j == i:
            return -1
       
        # swap s[i], s[j]
        s[i], s[j] = s[j], s[i]
        # print s, sorted(s[i+1:])
        resList = s[:i+1]+sorted(s[i+1:])
        res = int(''.join(resList))
        # check if res is a 32-bit value
        if res>2**31-1:
            return -1
        return res