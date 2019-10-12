class Solution(object):
    def backtrack(self, nums, path, res):
        if not nums:
             res.append(path)
        for i in range(len(nums)):
            if i == 0 or nums[i]!=nums[i-1]:
                self.backtrack(nums[:i]+nums[i+1:], path+[nums[i]], res)
        return 
    
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        res, path = [], []
        self.backtrack(nums, path, res)
        return res
    