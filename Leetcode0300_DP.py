class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Note that the numbers can be discontinuous
        # dp[i] means the length of the longest increasing sequence if 
        # it ends with nums[i]
        if not nums:
            return 0
        dp = [0]*len(nums)
        dp[0] = 1
        for i in range(1, len(nums)):
            currMaxLen = 1
            for j in range(i):
                if nums[i]>nums[j]:
                    currMaxLen = max(currMaxLen, dp[j]+1)
            dp[i] = currMaxLen
        # print dp 
        return max(dp)
