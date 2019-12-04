class Solution(object):
    def corpFlightBookings(self, bookings, n):
        """
        :type bookings: List[List[int]]
        :type n: int
        :rtype: List[int]
        """
        # Explanation
        #     Set the change of seats for each day.
        #     If booking = [i, j, k],
        #     it needs k more seat on ith day,
        #     and we don't need these seats on j+1th day.
        #     We accumulate these changes then we have the result           that we want.
        # Complexity
        #     Time O(booking + N) for one pass on bookings
        #     Space O(N) for the result
        
        res = [0]*(n+1)
        
        for i, j, k in bookings:
            res[i-1] += k
            res[j] -= k
        
        for i in range(1,n):
            res[i] += res[i-1]
        return res[:-1] 