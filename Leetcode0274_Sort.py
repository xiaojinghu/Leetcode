class Solution(object):

    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        # approach 1: sorting 
        citations.sort(reverse = True)
        print citations
        for i in range(len(citations)):
            if citations[i]>=i+1:
                if i == len(citations)-1 or citations[i+1]<=i+1:
                    return i+1
        return 0
        
