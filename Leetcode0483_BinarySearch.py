from math import pow, log
class Solution(object):
    def smallestGoodBase(self, n):
        """
        :type n: str
        :rtype: str
        """
        # find the smallest k such that (k^m-1)/(k-1)=n, where k and m
        # are both intergers and k>=2
        
        # the smallest k is 2, and the largest k is n-1
        # the smallest m is 2 when k=n-1, and the largest m is log2(n+1) when k=2
        # since the range of k is much larger than the range of m, we start iterating the m
        n = int(n)
        for m in range(int(log(n+1, 2)), 1, -1):
            start = 2
            # note that we need to adjust the range of k according to m
            # otherwise the pow function will overflow
            # we know n = 1+k+k^2+...+k^(m-1), so k^(m-1)<n
            # so k<pow(n, 1.0/(m-1))
            end = int(pow(n, 1.0/(m-1)))+1
            while(start+1<end):
                if m == 2:
                    print m, start, end
                middle = (start+end)/2
                currRes = (middle**m-1)/(middle-1)
                if currRes == n:
                    return str(middle)
                if currRes<n:
                    start = middle
                if currRes>n:
                    end = middle
            currRes = (start**m-1)/(start-1)
            if currRes == n:
                return str(start)
            currRes = (end**m-1)/(end-1)
            if currRes == n:
                return str(end)
        return str(n-1)
            
        