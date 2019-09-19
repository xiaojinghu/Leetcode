class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        if not citations:
            return 0
        
        start = 0
        end = len(citations)-1
        
        while(start+1<end):
            middle = (start+end)/2
            # we check if middle is h-index
            if citations[middle]>=len(citations)-middle:
                if middle == 0 or citations[middle-1]<=len(citations)-middle:
                    return len(citations)-middle
                else:
                    end = middle
            else:
                start = middle
                
        
        # we check if start and end satifies the condition
        if citations[start]>=len(citations)-start:
                if start == 0 or citations[start-1]<=len(citations)-start:
                    return len(citations)-start
                
        if citations[end]>=len(citations)-end:
                if end == 0 or citations[end-1]<=len(citations)-end:
                    return len(citations)-end
        return 0