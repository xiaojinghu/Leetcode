class Solution(object):
    def getDistance(self, List):
        # we can calculate the distance using two pointers
        i = 0
        j = len(List)-1
        distance = 0
        #Note that for every pair of (i,j), dis_i_to_median+dis_j_to_median = List[j]-List[i]
        while(i<j):
            distance += List[j]-List[i]
            i += 1
            j -= 1
        return distance


    def minTotalDistance(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """     
        if not grid or not grid[0]:
            return 0
        # since the x and y are independent while calculating the Manhattan distance, we can solve this problem by solve 2 1-D subproblems
        
        # first look at the x-axis, we know that the best meeting point must be locating soomewhere between the left-most and the right-most point.
        
        # As long as there is equal number of points to the left and right of the meeting point, the total distance is minimized.
        
        # we get the list of all x and y repectively
        x = []
        y = []
        # Note that x and y must be sorted so that we can find the median
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    x.append(i)
        for j in range(len(grid[0])):
            for i in range(len(grid)):
                if grid[i][j] == 1:
                    y.append(j)
        return self.getDistance(x)+self.getDistance(y)
