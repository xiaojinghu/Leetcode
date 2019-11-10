class Solution(object):
    def oddCells(self, n, m, indices):
        """
        :type n: int
        :type m: int
        :type indices: List[List[int]]
        :rtype: int
        """
        count = 0
        countflip = {}
        
        for row, col in indices:
            for j in range(m):
                if (row, j) not in countflip:
                    countflip[(row, j)] = 0
                countflip[(row, j)] += 1
            for i in range(n):
                if (i, col) not in countflip:
                    countflip[(i, col)] = 0
                countflip[(i, col)] += 1
            # print countflip
        for i, j in countflip:
            if countflip[(i,j)] %2 != 0:
                count += 1
        return count