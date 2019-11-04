class Solution(object):
    def gcd(self, a, b):
        if a<b:
            return self.gcd(b,a)
        if b==0:
            return a
        return self.gcd(b, a%b)
    
    def lcm(self, a, b):
        return a*b/(self.gcd(a,b))
    
    def count(self, middle, A, B, AB):
        countA = middle/A
        countB = middle/B
        countAB = middle/AB
        count = countA+countB-countAB
        return count
    
    def nthMagicalNumber(self, N, A, B):
        """
        :type N: int
        :type A: int
        :type B: int
        :rtype: int
        """
        AB = self.lcm(A, B)
        left = 1
        right = N*min(A, B)
        while(left+1<right):
            middle = (left+right)/2
            tolCount = self.count(middle, A, B, AB)
            if tolCount >= N:
                right = middle
            else:
                left = middle
                
        # check start and end
        if self.count(left, A, B, AB) == N:
            return left%(10**9+7)
        return right%(10**9+7)
                
            