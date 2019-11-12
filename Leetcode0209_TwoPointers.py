class Solution(object):
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        if sum(nums)<s:
            return 0
        
        # calculate the prefix sum
        prefixSum = [0]*(len(nums)+1)
        for i in range(len(nums)):
            prefixSum[i+1] = prefixSum[i]+nums[i]
        # print prefixSum
        i = 0
        j = 0
        minLen  = len(nums)
         
        while(j<len(prefixSum)):
            # here i<=j
            if prefixSum[j]-prefixSum[i]<s:
                # we need to move j right forward 
                j += 1
                continue
            while i<=j and prefixSum[j]-prefixSum[i] >= s:
                # print i, j, prefixSum[j]-prefixSum[i]
                minLen = min(minLen, j-i)
                i += 1
            # print i, j
            j += 1
                    
        return minLen