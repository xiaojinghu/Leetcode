class Solution(object):
    def minimumSwap(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: int
        """
        if len(s1)!=len(s2):
            return -1
        
        # count how many differences there are in s1
        countXToY = 0
        countYToX = 0
        for i in range(len(s1)):
            char1 = s1[i]
            char2 = s2[i]
            if char1 != char2:
                if char1 == 'x':
                    countXToY += 1
                if char1 == 'y':
                    countYToX += 1
                print char1, char2, countXToY, countYToX
        print countXToY, countYToX
        # first we swap between XToY and YToX
        pairXToY = countXToY/2
        pairYToX = countYToX/2
        print pairXToY, pairYToX
        # then we pair XToY and YToX
        if countXToY%2==0:
            if countYToX%2==0:
                return pairXToY + pairYToX
            else:
                return -1
        if countYToX%2==0:
            return -1
        return pairXToY+pairYToX+2