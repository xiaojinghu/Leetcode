class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        # idea: two steps
        # 1. flip the image along the right diagonal
        # 2. flip the image along the horizontal middle line
        n = len(matrix)
        
        # step1
        for i in range(n):
            for j in range(n):
                if i+j<=n-1:
                    matrix[i][j], matrix[n-1-j][n-1-i]=matrix[n-1-j][n-1-i], matrix[i][j]
        #step2
        for j in range(n):
            for i in range(n/2):
                matrix[i][j], matrix[n-1-i][j] = matrix[n-1-i][j], matrix[i][j]