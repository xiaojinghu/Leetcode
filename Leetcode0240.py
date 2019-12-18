class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        #从右上角开始, 比较target 和 matrix[i][j]的值。如果小于target, 则该行不可能有此数, 所以i++; 如果大于target, 则该列不可能有此数, 所以j--。遇到边界则表明该矩阵不含target.
        
        if not matrix or not matrix[0]:
            return False
        
        i = 0
        j = len(matrix[0])-1
        
        while(i<len(matrix) and j>=0):
            if matrix[i][j]==target:
                return True
            if matrix[i][j]>target:
                j -= 1
                continue
            if matrix[i][j]<target:
                i += 1
                continue
        return False
            
        
        