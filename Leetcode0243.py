class Solution(object):
    def shortestDistance(self, words, word1, word2):
        """
        :type words: List[str]
        :type word1: str
        :type word2: str
        :rtype: int
        """
        
        # THIS IS A 2 POINTER SOLUTION
        i = 0
        j = 0
        minDistance = len(words)
        # we make i point to word1 and j point to word2
        while(i<len(words) and j<len(words)):
            if words[i] != word1:
                i += 1
                continue
            # here i points to word1
            if words[j] != word2:
                j += 1
                continue
            # here words[i] points to word1 and j points to word2
            # now we calculate the distance
            if j>i:
                # this means word2 is behind word1
                minDistance = min(j-i, minDistance)
                i += 1
                continue
            else:
                minDistance = min(i-j, minDistance)
                j += 1
                continue           
        return minDistance
