class Solution(object):
    def backtrack(self, nums, res, path):
        # termination condition
        if not nums:
            res.append(path)
            return 
        for j in range(len(nums)):
            self.backtrack(nums[:j]+nums[j+1:], res, path+[nums[j]])
        return 
        
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res , path = [], []
        self.backtrack(nums, res, path)
        return res
