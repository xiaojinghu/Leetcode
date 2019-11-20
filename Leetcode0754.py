class Solution(object):
    def reachNumber(self, target):
        """
        :type target: int
        :rtype: int
        """
        # examples:
        # target=1, 1,            1 steps
        # target=2, 1-2+3         3 steps
        # target=3, 1+2           2 steps
        # target=4, -1+2+3        3 steps
        # target=5: -1+2+3-4+5    5 steps
        # we can see that for a target we need to find the minimum k such that (+/-)1(+/-)2(+-)3...(+-)k>=target.
        # since 1+2+3+4+...k = k(1+k)/2, so we know 
        # (k+1)^2>2*target
        # (k-1)^2<2*target
        #  sqrt(2*target)-1<k<sqrt(2*target)+1
        # there are two numbers in this range
        # if target is odd, then there must be odd odds in 1...k, and if target is even, there must be even odds in 1...k.
        target = abs(target)
        if target%2==1:
            k = int((2*target)**0.5)
            # check if k is the minimum k
            if (k-1)*k/2>=target or k*(k+1)/2<target:
                k += 1
            if k%2==0:
                # we need to determine how many odds there are
                # there are k/2 odd numbers before
                if (k/2)%2==0:
                    # even number of odds, we need one more odd
                    k += 1
            else:
                if ((k+1)/2)%2==0:
                    # even number of odds, we need one more odd
                    k += 2
                    
        if target%2==0:
            k = int((2*target)**0.5)
            print k
            if (k-1)*k/2>=target or k*(k+1)/2<target:
                k += 1
            print k
            if k%2==0:
                # we need to determine how many odds there are
                # there are k/2 odd numbers before
                if (k/2)%2==1:
                    # odd number of odds, we need one more odd
                    k += 1
            else:
                if ((k+1)/2)%2==1:
                    # odd number of odds, we need one more odd
                    k += 2
                    
        # once we get the minimum k that 1+2+3+4+....+k>=target, we definately can get target because we can always get (1+2+3+...+k-target) by turing some "+" to "-". 
        return k