class solution(object):
    def rotateOnce(self, matrix):
        n = len(matrix)
        for i in range(n):
            for j in range(n):
                if i!=j and i+j!=(n-1):
                    matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        for i in range(n):
            for j in range(n/2):
                if i!=j and i+j != n-1:
                    matrix[i][j], matrix[i][n-1-j] = matrix[n-1-j][i]

    def rotate(self, matrix, k):
        for i in range(k):
            self.rotate(matrix)

            