"""
   This is the custom function interface.
   You should not implement it, or speculate about its implementation
   class CustomFunction:
       # Returns f(x, y) for any given positive integers x and y.
       # Note that f(x, y) is increasing with respect to both x and y.
       # i.e. f(x, y) < f(x + 1, y), f(x, y) < f(x, y + 1)
       def f(self, x, y):
  
"""
class Solution(object):
    def findSolution(self, customfunction, z):
        """
        :type num: int
        :type z: int
        :rtype: List[List[int]]
        """
        res = []
        # first find the range of x
        max_x = 1
        while(customfunction.f(max_x,1)<z):
            max_x = 2 * max_x

        for x in range(1, max_x+1):
            # find the range of y
            max_y = 1
            while(customfunction.f(x,max_y)<z):
                max_y = 2*max_y  
            start_y = 1
            end_y = max_y
            flag = False
            while(start_y+1<end_y):
                middle_y = (start_y+end_y)/2
                if customfunction.f(x, middle_y) == z:
                    res.append([x, middle_y])
                    flag = True
                    break
                if customfunction.f(x, middle_y)<z:
                    start_y = middle_y
                else:
                    end_y = middle_y
            if not flag:
                if customfunction.f(x, start_y) == z:
                    res.append([x, start_y])
                elif customfunction.f(x, end_y) == z:
                    res.append([x, end_y])
        return res