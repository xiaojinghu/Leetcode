class Solution(object):
    def minDominoRotations(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: int
        """
        # the number to be rotated is either A[0] or B[0]
        
        # first we check A[0]
        countRotateA1 = 0
        countRotateA2 = 0
        flagA = True
        for i in range(len(A)):
            if A[i] == A[0] and B[i] == A[0]:
                continue
            if B[i] == A[0]:
                countRotateA1 += 1
            if A[i] == A[0]:
                countRotateA2 += 1
            if A[i]!=A[0] and B[i]!=A[0]:
                flagA = False
                break
            
        countRotateA = min(countRotateA1, countRotateA2)
        
        # second we check B[0]
        countRotateB1 = 0
        countRotateB2 = 0
        flagB = True
        for i in range(len(B)):
            if B[i] == B[0] and A[i] == B[0]:
                continue
            if A[i] == B[0]:
                countRotateB1 += 1
            if B[i] == B[0]:
                countRotateB2 += 1
            if A[i]!=B[0] and B[i] != B[0]:
                flagB = False
                break
            
        countRotateB = min(countRotateB1, countRotateB2)
        
        print flagA, flagB
        if flagA and flagB:
            return min([countRotateA, countRotateB])
        if flagB:
            return countRotateB
        if flagA:
            return countRotateA
        return -1
    
        