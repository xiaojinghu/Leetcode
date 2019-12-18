class Solution(object):
    def numMovesStones(self, a, b, c):
        """
        :type a: int
        :type b: int
        :type c: int
        :rtype: List[int]
        """
        abc = [a,b,c]
        abc.sort()
        a, b, c = abc
        gap_ab = b-a
        gap_bc = c-b
        
        if gap_ab == 1 and gap_bc == 1:
            minSteps = 0
        elif gap_ab == 1 or gap_bc == 1 or gap_ab == 2 or gap_bc == 2:
            minSteps = 1
        else:
            minSteps = 2
        
        maxSteps = gap_bc+gap_ab-2
        return [minSteps, maxSteps]