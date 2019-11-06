class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        
        Max = nums[0]
        currSum = 0
        for i in range(len(nums)):
            currSum += nums[i]
            Max = max(currSum, Max)
            if currSum < 0:
                currSum = 0
        return Max