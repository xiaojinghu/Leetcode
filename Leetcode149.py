class Solution(object):
    def maxPoints(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        if len(points)<=2:
            return len(points)
        
        # for each pair of nodes, calculate the slope, and then check how many times this slop appears
        res = 0
        for i in range(len(points)):
            # lines is used to count slops' occurances
            slopes = collections.defaultdict(int)
            duplicates = 0
            for j in range(i + 1, len(points)):
                if points[i][0] == points[j][0] and points[i][1] == points[j][1]:
                    # these two points are the same
                    duplicates += 1
                    continue
                dx = points[i][0] - points[j][0]
                dy = points[i][1] - points[j][1]
                delta = self.gcd(dx, dy)
                slopes[(dx / delta, dy / delta)] += 1
            # note that duplicates count as different points
            res = max(res, (max(slopes.values()) if slopes else 0)+1 + duplicates)
        return res
                
    def gcd(self, x, y):
        # gcd(a,b) = gcd(b,a mod b)
        return x if y == 0 else self.gcd(y, x % y)