class Solution(object):
    def longestSubsequence(self, arr, difference):
        """
        :type arr: List[int]
        :type difference: int
        :rtype: int
        """
        endToLen = {}
        if not arr:
            return 0
        maxLen = 1
        
        for num in arr:
            #first check if we can append it to some subsequence
            if num-difference in endToLen:
                length = endToLen[num-difference]
                # pop the old length out
                endToLen.pop(num-difference)
                # add the new end and the new length
                endToLen[num] = length+1
                maxLen = max([maxLen, length+1])
                continue
            if num not in endToLen:
                endToLen[num] = 1
        return maxLen
            