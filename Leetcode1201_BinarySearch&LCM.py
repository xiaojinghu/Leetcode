class Solution(object):
    def gcd(self, a, b):
        if a<b:
            a, b = b, a
            return self.gcd(a, b)
        if b == 0:
            return a
        return self.gcd(b, a%b)
    
    def lcm(self, a, b):
        return a*b/self.gcd(a,b)
        
    def nthUglyNumber(self, n, a, b, c):
        """
        :type n: int
        :type a: int
        :type b: int
        :type c: int
        :rtype: int
        """
        # Brute Force: to find an ugly number we need to find all multiples of a, b and c, remove the duplicates and sort them. But consider the scale of the dataset, time solution will obviously result in TLE.
        # so we need to use binary search and LCM(least common multiple). Given a k, we count how many ugly numbers there are in range [1, k] so that we can determine which range to search. 
        # The key point is, since there are many duplicates in multiples of a, b and c, how could we count accurately. We can use inclusion-exclusion priciple. 
        # for multiples of a,b and c, there are 7 possibilities in general: a, b, c, ab, ac, bc, abc.
        # take a=2, b=3, c=5 as an example. 
        # 2: 1*2, 2*2, 3*2, 4*2, 5*2, 6*2...
        # 3: 1*3, 2*3, 3*3, 4*3, 5*3, 6*3...
        # 5: 1*5, 2*5, 3*5, 4*5, 5*5, 6*5...
        # count of numbers that can be divided by 2: k/2, marked as count_a.
        # count of numbers that can be divided by 3: k/3, marked as count_b
        # count of numbers that can be divided by 5: k/5, marked as count_c
        # count of numbers that can be divided by 2 and 3: k/6, marked as count_ab
        # count of numbers that can be divided by 2 and 5: k/10, marked as count_ac
        # count of numbers that can be divided by 3 and 5: k/15, marked as count_bc
        # count of numbers that can be divided by 2, 3 and 5: k/30, marked as count_abc
        # total count: count_a+count_b+count_c-count_ab-count_bc-count_ac+count_abc. Easy to see if draw an venn diagram.
        left = 1
        right = 2*(10**9)
        ab = self.lcm(a, b)
        ac = self.lcm(a,c)
        bc = self.lcm(b,c)
        abc = self.lcm(a, bc)
        while(left+1<right):
            middle = (left+right)/2
            count = middle/a+middle/b+middle/c-middle/ab - middle/bc-middle/ac+middle/abc
            if count>=n:
                right = middle
            else:
                left = middle
        # check left
        middle = left
        count = middle/a+middle/b+middle/c-middle/ab - middle/bc-middle/ac+middle/abc
        if count == n:
            return left
        return right