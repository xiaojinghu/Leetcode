class Solution(object):
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        if num == 0:
            return [0]
        if num == 1:
            return [0,1]
        if num == 2:
            # res = [0, 1, 1]
            return [0, 1, 1]
        res = [0, 1, 1]
        for i in range(3, num+1):
            if i%2==1:
                # them i is odd, (i-1) must be even, we can simply add 1
                res.append(res[i-1]+1)
                continue
            # i is even, then i-1 must be odd
            # the the last bit must change from 1 to 0 and  we are adding
            # and 1 to (i-1)/2
            res.append(res[(i-1)/2+1])
        return res